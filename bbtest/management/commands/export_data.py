from django.core.management.base import BaseCommand
from bbtest.models import User
from datetime import datetime, timedelta
import pytz
from bbtest.models import Quiz, TestSection
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from django.db import connection, reset_queries
from django.db.models import Q
import time
from functools import lru_cache


class Command(BaseCommand):
    help = '''export student data
    scp darkhan@compact-102.bbtest.kz:~/BBEdu/export.xlsx ./export.xlsx
    ''' 

    def add_arguments(self, parser):
        dt = timedelta(days=30)
        option = ["SIMPLE", "FORMAT", "REGISTER"]
        parser.add_argument('option', type=str, nargs='?', choices=option, default="FORMAT")
        parser.add_argument("start_date", nargs='?', 
                            default=datetime.now(tz=pytz.timezone('Asia/Almaty')) - dt, 
                            # type=datetime,
                            type=lambda d: datetime.strptime(d, '%Y-%m-%d')
                            )
        parser.add_argument('end_date', nargs='?', 
                             default=datetime.now(tz=pytz.timezone('Asia/Almaty')), 
                            #  type=datetime
                             type=lambda d: datetime.strptime(d, '%Y-%m-%d')
                             )
        

        # print(parser.parse_args(["-s", "2022-01-01"]))

    def handle(self, *args, **kwargs):

        # form = ExportDataForm(data=request.POST)
        # valid = form.is_valid()    # is_valid should be called before form.cleaned_data could be accessed
        start_date = kwargs["start_date"]  # datetime(2021, 8, 31, 0, 0, 0, tzinfo=pytz.timezone('Asia/Almaty'))
        end_date = kwargs["end_date"]      # datetime(2021, 8, 31, 0, 0, 0, tzinfo=pytz.timezone('Asia/Almaty'))
        try:
            start_date = pytz.timezone('Asia/Almaty').localize(start_date, is_dst=None)
        except ValueError:
            pass
        try:
            end_date = pytz.timezone('Asia/Almaty').localize(end_date, is_dst=None)
        except ValueError:
            pass
        option = kwargs["option"]

        if not (end_date >= start_date):
            print("start_date > end_date")
            return

        # Create excel writer object in memory
        with open("export.xlsx", "wb") as file:
            workbook = xlsxwriter.Workbook(file, options={'remove_timezone': True})

            # reset_queries()
            start_queries = len(connection.queries)
            start = time.perf_counter()
            
            if option == "SIMPLE":
                self.simple_export(start_date, end_date, workbook)
            elif option == "FORMAT":
                self.formatted_export(start_date, end_date, workbook)
            elif option == "REGISTER":
                self.register_export(start_date, end_date, workbook)

            workbook.close()
            end_queries = len(connection.queries)
            end = time.perf_counter()

            print("Export from {} to {}. n_queries={}, t={:.2f}s".format(start_date, end_date, end_queries-start_queries, (end - start)))
            return 

    @staticmethod
    @lru_cache(maxsize=None)
    def excel_offset_for_test(domain_id):
        res = TestSection.objects.filter(Q(domain_id=domain_id)).order_by("order")

        offset = {}
        # offset["student"] = (0, 1)
        end = 1
        for section in res:
            start = end + 1
            end = end + section.question_count + 4
            offset[section.name] = (start, start+4, section.question_count)
        return offset, end+1


    def formatted_export(self, start_date, end_date, workbook):
        date_format = workbook.add_format({'num_format': 'dd-mm-yy hh:mm:ss', 'align': 'left'})
        for domain_id in [7911]:
            quizes = Quiz.objects.filter(
                                    Q(test__bundle__isnull=False) & Q(started_at__lte=end_date) & Q(started_at__gte=start_date) & Q(test__section__domain=domain_id)
                                ).order_by("quiz_set__student", "test__bundle").prefetch_related("test", "test__questions", "test__section", "quiz_set", "quiz_set__student").iterator()
            worksheet = workbook.add_worksheet("{}_bundle".format(domain_id))
            if not quizes:  # empty response
                continue
            
            # create table header
            worksheet.write_row(0, 0, ["student", "lang"])
            offsets, last_col = self.excel_offset_for_test(domain_id)
            for sect_name, (s, m, c) in offsets.items():
                worksheet.write_row(0, s, ["{}_code".format(sect_name), "{}_started_at".format(sect_name), "{}_score".format(sect_name), "{}_max_score".format(sect_name)])
                worksheet.write_row(0, m, ["{}_{}".format(i+1, sect_name) for i in range(c)])
            worksheet.write(0, last_col, "Total")
            # worksheet.write(0, last_col+1, "Bundle")
            

            pointer = {sect_name: 1 for sect_name in offsets.keys()}  # stores row offset for subjects
            pr_student = None
            pr_bundle = None

            for i, quiz in enumerate(quizes):
                student = quiz.quiz_set.student.username + " | " + quiz.quiz_set.student.email
                bundle = quiz.test.bundle
                if student != pr_student or bundle != pr_bundle:
                    pointer = {sect_name: max(pointer.values()) for sect_name in offsets.keys()} 
                    pr_student = student
                    pr_bundle = bundle
                
                test_name = quiz.test.section.name
                col_offset = offsets[test_name][0]
                row_offset = pointer[test_name]

                code = quiz.test.code
                started = quiz.started_at
                score = quiz.score()
                max_score = quiz.test.max_score()
                row = [bundle + "|" + code, started, score, max_score] + quiz.get_student_answers()

                worksheet.write_row(row_offset, 0, [student, bundle[:2]])  # will be overwritten several times, but it is OK, overhead is acceptable
                worksheet.write_row(row_offset, col_offset, row)
                worksheet.write_datetime(row_offset, col_offset+1, started, date_format)
                pointer[test_name] += 1

                # for NIS test compute Total column
                n_rows_total = max(pointer.values())
                score_cols = [s+2 for s, _, _ in offsets.values()]
                for i in range(1, n_rows_total):
                    formula = [xl_rowcol_to_cell(i, col) for col in score_cols]
                    worksheet.write_formula(i, last_col, '=' + "+".join(formula))
                    
        for domain_id in [7911, 7912, 7913, 7914, 7915, 7916, 7917]:
            quizes = Quiz.objects.filter(
                                    Q(started_at__lte=end_date) & Q(started_at__gte=start_date) & Q(test__section__domain=domain_id)
                                ).order_by("quiz_set__student", "test__language").prefetch_related("test", "test__questions", "test__section", "quiz_set", "quiz_set__student").iterator()
            worksheet = workbook.add_worksheet("{}".format(domain_id))
            if not quizes:  # empty response
                continue
            
            # create table header
            worksheet.write_row(0, 0, ["student", "lang"])
            offsets, last_col = self.excel_offset_for_test(domain_id)
            for sect_name, (s, m, c) in offsets.items():
                worksheet.write_row(0, s, ["{}_code".format(sect_name), "{}_started_at".format(sect_name), "{}_score".format(sect_name), "{}_max_score".format(sect_name)])
                worksheet.write_row(0, m, ["{}_{}".format(i+1, sect_name) for i in range(c)])
            if domain_id == 7911: worksheet.write(0, last_col, "Total")
            

            pointer = {sect_name: 1 for sect_name in offsets.keys()}  # stores row offset for subjects
            pr_student = None
            pr_lang = None

            for i, quiz in enumerate(quizes):
                student = quiz.quiz_set.student.username
                lang = quiz.test.language
                if student != pr_student or lang != pr_lang:
                    pointer = {sect_name: max(pointer.values()) for sect_name in offsets.keys()} 
                    pr_student = student
                    pr_lang = lang
                
                test_name = quiz.test.section.name
                col_offset = offsets[test_name][0]
                row_offset = pointer[test_name]

                code = quiz.test.code
                started = quiz.started_at
                score = quiz.score()
                max_score = quiz.test.max_score()
                row = [code, started, score, max_score] + quiz.get_student_answers()

                worksheet.write_row(row_offset, 0, [student, lang])  # will be overwritten several times, but it is OK, overhead is acceptable
                worksheet.write_row(row_offset, col_offset, row)
                worksheet.write_datetime(row_offset, col_offset+1, started, date_format)
                pointer[test_name] += 1

            if domain_id == 7911:   # for NIS test compute Total column
                n_rows_total = max(pointer.values())
                score_cols = [s+2 for s, _, _ in offsets.values()]
                for i in range(1, n_rows_total):
                    formula = [xl_rowcol_to_cell(i, col) for col in score_cols]
                    worksheet.write_formula(i, last_col, '=' + "+".join(formula))
                            
    def simple_export(self, start_date, end_date, workbook):
        for domain_id in [7911, 7912, 7913, 7914, 7915, 7916, 7917]:
            quizes = Quiz.objects.filter(
                                    Q(started_at__lte=end_date) & Q(started_at__gte=start_date) & Q(test__section__domain=domain_id)
                                ).order_by("quiz_set__student", "test__language").prefetch_related("test", "test__questions", "test__section", "quiz_set", "quiz_set__student").iterator() #.prefetch_related("user_permissions__content_type")  .order_by("-started_at")
            
            worksheet = workbook.add_worksheet("{}".format(domain_id))
            
            if not quizes:  # empty response
                continue
            
            worksheet.write_row(0, 0, ["student", "phone", "email", "test_name", "lang", "code", "started", "score", "max_score"] + ["Q{}".format(i) for i in range(1,61)])

            for i, quiz in enumerate(quizes):
                student = quiz.quiz_set.student.username
                phone = quiz.quiz_set.student.phone
                email = quiz.quiz_set.student.email
                lang = quiz.test.language
                code = quiz.test.code
                started = quiz.started_at
                test_name = quiz.test.section.name
                score = quiz.score()
                max_score = quiz.test.max_score()

                row = [student, phone, email, test_name, lang, code, started, score, max_score] + quiz.get_student_answers()
                worksheet.write_row(i+1, 0, row)


    def get_quizes_in_range(self, start_date, end_date):
        quizes = Quiz.objects.filter(
                                    Q(started_at__lte=end_date) & Q(started_at__gte=start_date)
                                ).order_by("-started_at").iterator() #.prefetch_related("user_permissions__content_type")
        table_tests_all = {}
        for quiz in quizes:
            student = (quiz.quiz_set.student.username, quiz.test.language)
            # student_email = quiz.quiz_set.student.email
            started = quiz.started_at
            test_name = quiz.test.section.name
            score = quiz.score()
            max_score = quiz.test.max_score()
            
            # print(student, ended, test_name, score, max_score)
            if student[1] != "xx":
                table_tests_all[student] = table_tests_all.get(student, {})
                table_tests_all[student][test_name]  = [started, score, max_score] + quiz.get_student_answers()
            else:
                for lang in ["ru", "kk"]:
                    student = (student[0], lang)
                    table_tests_all[student] = table_tests_all.get(student, {})
                    table_tests_all[student][test_name]  = [started, score, max_score] + quiz.get_student_answers()
        
        students_all = {s[0] for s in table_tests_all.keys()}
        for sname in students_all:
            count_ru = len(table_tests_all.get((sname, "ru"), {}).keys())
            count_kk = len(table_tests_all.get((sname, "kk"), {}).keys())
            if count_ru == count_kk and count_ru == 1 and "English Language" in table_tests_all.get((sname, "ru"), {}).keys() and "English Language" in table_tests_all.get((sname, "kk"), {}).keys():
                table_tests_all.pop((sname, "kk"), None)
            elif count_ru > count_kk:
                table_tests_all.pop((sname, "kk"), None)
            elif count_ru < count_kk:
                table_tests_all.pop((sname, "ru"), None)
        return table_tests_all

    def create_table_header(self, test_names_sorted, test_names_and_count):
        header = ["student", "lang"]
        # positions = {name: None for name in test_names_sorted}
        for k in test_names_sorted:
            # positions[k] = len(header) 
            header += ["{}_started".format(k), "{}_score".format(k), "{}_max_score".format(k)] + ["{}_{:03}".format(k, i+1) for i in range(test_names_and_count[k])]
            # positions[k]["end"] = len(header)

        
        header.append("Total_score")
        return header #, positions

    def write_response_csv(self, worksheet, table_tests_all, test_names_sorted, test_names_and_count):
        table = []
        for student, tests in table_tests_all.items():  # [(quiz.language, student)][test_name]
            table_row = [student[0], student[1]]   # name, lang
            total_score = 0
            for test_name in test_names_sorted:
                test_report = tests.get(test_name, None)
                if test_report is not None:     # if student attended this test
                    table_row += test_report
                    total_score += test_report[1]  # [1] -> score
                else:                           # if not attended generate empty 
                    table_row += [None for _ in range(test_names_and_count[test_name]+3)]
            # writer.writerow(table_row + [total_score])
            table.append(table_row + [total_score])
        
        table = sorted(table, key=lambda tup: (tup[0],tup[1]) )
        return table


    def register_export(self, start_date, end_date, workbook):
        date_format = workbook.add_format({'num_format': 'dd-mm-yyyy hh:mm:ss', 'align': 'left'})
        users = User.objects.filter(
                                Q(joined_at__lte=end_date) & Q(joined_at__gte=start_date) & Q(is_superuser=False)
                            ).iterator() 
        
        worksheet = workbook.add_worksheet("Users")
        
        if not users:  # empty response
            return 
        
        worksheet.write_row(0, 0, ["username", "first_name", "last_name", "phone", "email", "joined_at", "last_login", "is_active", "meta_data"])

        for i, user in enumerate(users):
            username = user.username
            first_name = user.first_name
            last_name = user.last_name
            phone = user.phone
            email = user.email
            joined_at = user.joined_at
            last_login = user.last_login
            is_active = user.is_active
            meta_data = str(user.meta_data)


            row = [username, first_name, last_name, phone, email, joined_at, last_login, is_active, meta_data]
            worksheet.write_row(i+1, 0, row)
            if type(joined_at) == datetime: worksheet.write_datetime(i+1, 5, joined_at, date_format)
            if type(last_login) == datetime: worksheet.write_datetime(i+1, 6, last_login, date_format)