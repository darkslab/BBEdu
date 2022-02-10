from django.core.management.base import BaseCommand
import re
from imap_tools import MailBox, AND, MailMessageFlags
from decimal import Decimal
from bbtest.models import User
from bbtest.models.accounting import Entry, Debit, Credit
# from django.core.mail import mail_admins
from time import sleep
from django.conf import settings
from datetime import datetime

def process_msg(msg):
    # # Print form and subject
    # print(msg.from_, ': ', msg.subject)
    # # Print the plain text (if there is one)
    # # print(msg.text)
    if len(msg.text) > 0:
        parsed_id, deposit = parse_mail_kaspi(msg.text)
    else:
        parsed_id, deposit = parse_mail_kaspi(msg.html)
    # print("ID: {}, amount: {}".format(parsed_id, deposit))
    # print()
    if parsed_id is None or deposit is None:
        Errors = "ID or deposit amount was not parsed corrctly\n"
        Errors += "[{}]\n\n".format(msg.subject)
        Errors += "[{}]\n\n".format(msg.text)
        Errors += "[{}]\n\n".format(msg.html)
        return Errors
    if float(deposit) <= 0:
        Errors = "Deposit amount [{}] is less than 0\n".format(deposit)
        Errors += "[{}]".format(msg.subject)
        return Errors
    try:
        # Deposit money
        usr = User.objects.get(id=int(parsed_id))
        Entry.objects.post("KaspiApp Automated", [
            Debit("Cash", Decimal(deposit)),
            Credit(usr.balance_account(), Decimal(deposit)),
        ])
    except User.DoesNotExist:
        Errors = "Could not find user {}, payment {}\n".format(parsed_id, deposit)
        Errors += "[{}]".format(msg.subject)
        return Errors
    return None


def parse_mail_kaspi(text):
    parsed_id = None
    deposit = None
    for line in text.split("\n"):
        line = line.strip()
        if len(line) == 0: continue
        # print(line)
        r = re.search(r"Номер личного.+= (\d+)", line)
        if r: parsed_id = r.group(1)
        r = re.search(r"Платеж на сумму: ([.\d]+)", line)
        if r: deposit = r.group(1)
    return parsed_id, deposit

# decorator to run aways
def retry_always(func):
    def inner(self, *args, **kwargs):
        while True:
            try:
                func(self, *args, **kwargs)
            except Exception as e:
                print()
                print(e)    
    return inner

def now_str():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Command(BaseCommand):
    help = 'runs kaspi payment email service' 
    counter = 1

    @retry_always
    def handle(self, *args, **kwargs):
        while True:
            with MailBox(settings.SECRETS["KASPI_IMAP"]).login(settings.SECRETS["KASPI_EMAIL"], settings.SECRETS["KASPI_EMAIL_TOKEN"]) as mb:
                count_new = 0
                count_from_kaspi = 0
                to_print = ""
                messages = mb.fetch(criteria=AND(seen=False), mark_seen=False, bulk=False)
                for msg in messages:
                    count_new += 1
                    if msg.from_ != settings.SECRETS["KASPI_FROM"]: continue
                    count_from_kaspi += 1
                    errors = process_msg(msg)
                    if errors is None:
                        # print()
                        # print("  ", now_str(), '->', msg.uid, "->", msg.from_, '->', msg.subject)
                        to_print += "\n-> {}: {} : {} -> {}".format(now_str(), msg.uid, msg.from_, msg.subject)
                        mb.flag(msg.uid, MailMessageFlags.SEEN, True)
                        mb.move(msg.uid, "KaspiDone")
                    else:
                        print(errors)
                        mb.move(msg.uid, "KaspiError")
                        # mail_admins("Kaspi Payment Automation Error", errors)

                print("{} [{}/{}] {:5} {}".format(now_str(), count_from_kaspi, count_new, self.counter, " "*10), end="\r")
                if len(to_print): print(to_print)
                sleep(60*2)
                self.counter += 1
