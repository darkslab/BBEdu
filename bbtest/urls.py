from django.urls import re_path
from .auth.views import (
    LoginView,
    LogoutView,
    RegisterView,
    RegisterDeveloperView,
    RegisterDemoUserView,
    PasswordResetView,
    PasswordResetConfirmView,
    RegisterB2BTeacherView,
)
from .views.base import (
    HomeView,
    DashboardView,
    SettingsView,
    BuyCreditsView,
    BuyCreditsQazkomView,
    BuyCreditsBeelineView,
    BuyCreditsBeelineActionView,
    TermsView,
    ContactUsView,
    FaqView,
)
from .views.upload import UploadStartView, UploadCompleteView, UploadAdoptView
from .views.test import (
    TestsView            as BuildTestsView,
    TestView             as BuildTestView,
    TestQuestionView     as BuildTestQuestionView,
    TestParagraphsView   as BuildTestParagraphsView,
    TestAttributesView   as BuildTestAttributesView,
    ApproveTestView      as BuildApproveTestView,
    RefuseTestView       as BuildRefuseTestView,
    DeleteTestView       as BuildDeleteTestView,
    ReDraftTestView      as BuildReDraftTestView,
    ReApproveTestView    as BuildReApproveTestView,
    ActivateTestView     as BuildActivateTestView,
    DeactivateTestView   as BuildDeactivateTestView,
    ToggleFreeTestView   as BuildToggleFreeTestView,
    CheckTestView        as BuildCheckTestView,
    TestPreviewView      as BuildTestPreviewView,
    TestPreviewDataView  as BuildTestPreviewDataView,
)
from .views.standalone_question import (
    StandaloneQuestionView              as BuildStandaloneQuestionView,
    StandaloneQuestionPreviewView       as BuildStandaloneQuestionPreviewView,
    StandaloneQuestionPreviewDataView   as BuildStandaloneQuestionPreviewDataView,
    StandaloneQuestionQuestionView      as BuildStandaloneQuestionQuestionView,
    StandaloneQuestionParagraphsView    as BuildStandaloneQuestionParagraphsView,
    StandaloneQuestionAttributesView    as BuildStandaloneQuestionAttributesView,
    StandaloneQuestionSendCommentView   as BuildStandaloneQuestionSendCommentView,

    ApproveQuestionView      as BuildApproveStandaloneQuestionView,
    RefuseQuestionView       as BuildRefuseStandaloneQuestionView,
    DeleteQuestionView       as BuildDeleteStandaloneQuestionView,
    ReDraftQuestionView      as BuildReDraftStandaloneQuestionView,
    ReApproveQuestionView    as BuildReApproveStandaloneQuestionView,
    ActivateQuestionView     as BuildActivateStandaloneQuestionView,
    DeactivateQuestionView   as BuildDeactivateStandaloneQuestionView,
    CheckQuestionView        as BuildCheckStandaloneQuestionView,
    # ToggleFreeQuestionView   as BuildToggleFreeTestView,

)
from .views.package import (
    BuildPackagesView             as BuildPackagesView,
    CreatePackageFormView         as BuildCreatePackageFormView,
    BuildPackageView              as BuildPackageView,
    BuildStudentGroupView         as BuildStudentGroupView,
    ManagePackageStudentsFormView,
    ManagePackageCreateStudentGroupFormView,
    ManagePackageTestFormView,
    RemoveTestFromPackageView,
    FinalizePackageView,
    ActivateStudentGroupToggleView,
    ActivateStudentTurnOFF,
    ActivateStudentTurnON,
)

from .views.student import (
    DashboardView         as StudentDashboardView,
    BuyTestDomainsView    as StudentBuyTestDomainsView,
    BuyTestsView          as StudentBuyTestsView,
    BuyTestsCartView      as StudentBuyTestsCartView,
    BuyTestsCheckoutView  as StudentBuyTestsCheckoutView,
    ExamView              as StudentExamView,
    ExamContinueView      as StudentExamContinueView,
    ExamStartView         as StudentExamStartView,
    ExamSkipView          as StudentExamSkipView,
    ExamEndView           as StudentExamEndView,
    ExamReportView        as StudentExamReportView,
    ResultsView           as StudentResultsView,
    ResultView            as StudentResultView,
    ResultDataView        as StudentResultDataView,
    TransactionsView      as StudentTransactionsView,
    TransactionView       as StudentTransactionView,
)
from .views.demouser import (
    DashboardView         as DemouserDashboardView,
)
from .views.developer import (
    DashboardView        as DeveloperDashboardView,
    AcknowledgementView  as DeveloperAcknowledgementView,
    TestsView            as DeveloperTestsView,
    OfferView            as DeveloperOfferView,
)
from .views.super import (
    DashboardView                 as SuperDashboardView,
    TestsView                     as SuperTestsView,
    QuestionView                  as SuperQuestionView,
    DownloadSubscriptionListView  as SuperDownloadSubscriptionListView,
    UsersView                     as SuperUsersView,
    UserView                      as SuperUserView,
    ImpersonateUserView           as SuperImpersonateUserView,
    GiveCreditsUserView           as SuperGiveCreditsUserView,
    ChangePassManualView          as SuperChangePassManualView,
    QuizzesView                   as SuperQuizzesView,
    TrialBalanceView              as SuperTrialBalanceView,
    CreateStudentsView            as SuperCreateStudentsView,
    CreateStudentsFormView        as SuperCreateStudentsFormView,
    ExportDataView                as SuperExportDataView,
    ExportDataFormView            as SuperExportDataFormView,
    CreateQuizSetDublicateView,

    
)
from .views.test_bank import (
    BuildSelectTestForAssembleView,
    BuildTestAssembleView,
    BuildStandaloneQuestionCreateView,
)


app_name = "bbtest"
urlpatterns = [
    # PUBLIC URLS
    re_path(r"^$",            HomeView.as_view(),      name="home"      ),
    re_path(r"^contact-us/$", ContactUsView.as_view(), name="contact_us"),

    # USER URLS
    re_path(r"^dashboard/$",                                       DashboardView.as_view(),               name="dashboard"                 ),
    re_path(r"^settings/$",                                        SettingsView.as_view(),                name="settings"                  ),

    # UPLOAD URLS
    re_path(r"^uploads/start/$",                              UploadStartView.as_view(),    name="upload_start"   ),
    re_path(r"^uploads/(?P<uuid>[0-9A-Fa-f]{32})/complete/$", UploadCompleteView.as_view(), name="upload_complete"),
    re_path(r"^uploads/(?P<uuid>[0-9A-Fa-f]{32})/adopt/$",    UploadAdoptView.as_view(),    name="upload_adopt"   ),

    # TEST BUILDING URLS
    re_path(r"^build/tests/$",                                                                           BuildTestsView.as_view(),              name="build_tests"            ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/$",                                                BuildTestView.as_view(),               name="build_test"             ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/)?$",            BuildTestQuestionView.as_view(),       name="build_test_question"    ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/paragraphs/)?$", BuildTestParagraphsView.as_view(),     name="build_test_paragraphs"  ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/attributes/$",                                     BuildTestAttributesView.as_view(),     name="build_test_attributes"  ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/approve/$",                                        BuildApproveTestView.as_view(),        name="build_approve_test"     ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/redraft/$",                                        BuildReDraftTestView.as_view(),        name="build_redraft_test"     ), 
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/reapprove/$",                                      BuildReApproveTestView.as_view(),      name="build_reapprove_test"   ), 
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/activate/$",                                       BuildActivateTestView.as_view(),       name="build_activate_test"    ), 
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/deactivate/$",                                     BuildDeactivateTestView.as_view(),     name="build_deactivate_test"  ), 
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/refuse/$",                                         BuildRefuseTestView.as_view(),         name="build_refuse_test"      ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/delete/$",                                         BuildDeleteTestView.as_view(),         name="build_delete_test"      ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/toggle-free/(?P<free>true|false)/$",               BuildToggleFreeTestView.as_view(),     name="build_toggle_free_test" ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/check/$",                                          BuildCheckTestView.as_view(),          name="build_check_test"       ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview/$",                                        BuildTestPreviewView.as_view(),        name="build_test_preview"     ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview-data/$",                                   BuildTestPreviewDataView.as_view(),    name="build_test_preview_data"),

    re_path(r"^build/test_assemble/$",                                                                     BuildSelectTestForAssembleView.as_view(),              name="build_assemble_tests"            ),
    re_path(r"^build/test_assemble/(?P<code>[0-9A-Fa-f]{4,6})/$",                                          BuildTestAssembleView.as_view(),                       name="build_assemble_variant"            ),

    re_path(r"^build/questions/$",                                                                           SuperQuestionView.as_view(),                         name="questions"      ),
    re_path(r"^build/questions/create/$",                                                                    BuildStandaloneQuestionCreateView.as_view(),         name="question_create"      ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/$",                                               BuildStandaloneQuestionView.as_view(),               name="build_standalone_question"    ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/question/$",                                      BuildStandaloneQuestionQuestionView.as_view(),       name="build_standalone_question_question"    ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/question/(?P<code3>[0-9A-Za-z]{1,15})/$",         BuildStandaloneQuestionQuestionView.as_view(),       name="build_standalone_question_question2"    ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/attributes/$",                                    BuildStandaloneQuestionAttributesView.as_view(),     name="build_standalone_question_attributes"  ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/paragraphs/$",                                    BuildStandaloneQuestionParagraphsView.as_view(),     name="build_standalone_question_paragraphs"  ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/paragraphs/(?P<code3>[0-9A-Za-z]{1,15})/paragraphs/$",                                    BuildStandaloneQuestionParagraphsView.as_view(),     name="build_standalone_question_paragraphs"  ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/preview/$",                                       BuildStandaloneQuestionPreviewView.as_view(),        name="build_standalone_question_preview"  ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/preview-data/$",                                  BuildStandaloneQuestionPreviewDataView.as_view(),    name="build_standalone_question_preview_data"  ),
    # re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/approve/$",                                       BuildApproveTestView.as_view(),                      name="build_approve_question"     ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/send_comment/$",                                   BuildStandaloneQuestionSendCommentView.as_view(),    name="build_standalone_question_send_comment"  ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/approve/$",                                        BuildApproveStandaloneQuestionView.as_view(),        name="build_approve_standalone_question"     ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/redraft/$",                                        BuildReDraftStandaloneQuestionView.as_view(),        name="build_redraft_standalone_question"     ), 
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/reapprove/$",                                      BuildReApproveStandaloneQuestionView.as_view(),      name="build_reapprove_standalone_question"   ), 
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/activate/$",                                       BuildActivateStandaloneQuestionView.as_view(),       name="build_activate_standalone_question"    ), 
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/deactivate/$",                                     BuildDeactivateStandaloneQuestionView.as_view(),     name="build_deactivate_standalone_question"  ), 
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/refuse/$",                                         BuildRefuseStandaloneQuestionView.as_view(),         name="build_refuse_standalone_question"      ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/delete/$",                                         BuildDeleteStandaloneQuestionView.as_view(),         name="build_delete_standalone_question"      ),
    re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/check/$",                                          BuildCheckStandaloneQuestionView.as_view(),          name="build_check_standalone_question"       ),
    # re_path(r"^build/questions/(?P<code>[0-9A-Za-z]{1,15})/toggle-free/(?P<free>true|false)/$",               BuildToggleFreeTestView.as_view(),     name="build_toggle_free_test" ),


    re_path(r"^build/packages/$",                                                                                   BuildPackagesView.as_view(),                name="build_packages" ),
    re_path(r"^build/create-package/create-form/$",                                                                 BuildCreatePackageFormView.as_view(),       name="build_create_package_form"),

    re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/$",                                               BuildPackageView.as_view(),                 name="build_package" ),
    re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/(?P<student_group_id>\d+)?$",                     BuildStudentGroupView.as_view(),            name="build_student_group" ),
    re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/(?P<student_group_id>\d+)?/add-students/$",       ManagePackageStudentsFormView.as_view(),    name="build_package_add_students" ),
    # re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/(?P<student_group_id>\d+)?/toggle-group/$",       ActivateStudentGroupToggleView.as_view(),   name="build_toggle_student_group"),
    re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/(?P<student_group_id>\d+)?/turnon-group/$",       ActivateStudentTurnON.as_view(),            name="build_turnon_student_group"),
    re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/(?P<student_group_id>\d+)?/turnoff-group/$",      ActivateStudentTurnOFF.as_view(),           name="build_turnoff_student_group"),

    re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/add-test/$",                                      ManagePackageTestFormView.as_view(),        name="build_package_add_test" ),
    re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/create-student-group/$",                          ManagePackageCreateStudentGroupFormView.as_view(),    name="build_package_create_student_group" ),
    re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/activate-package/$",                              FinalizePackageView.as_view(),              name="build_activate_package" ),
    re_path(r"^build/packages/(?P<package_code>[0-9A-Fa-f]{6,10})/(?P<test_code>[0-9A-Fa-f]{4,6})/remove-test/$",   RemoveTestFromPackageView.as_view(),        name="build_remove_test_from_package" ),

    # STUDENT URLS
    re_path(r"^student/$",                                            StudentDashboardView.as_view(),        name="student_dashboard"         ),
    re_path(r"^student/select-tests/$",                               StudentBuyTestDomainsView.as_view(),   name="student_buy_test_domains"  ),
    re_path(r"^student/select-tests/(?P<test_domain_id>\d+)/$",       StudentBuyTestsView.as_view(),         name="student_buy_tests"         ),
    re_path(r"^student/select-tests/(?P<test_domain_id>\d+)/cart/$",  StudentBuyTestsCartView.as_view(),     name="student_buy_tests_cart"    ),
    re_path(r"^student/select-tests/checkout/$",                      StudentBuyTestsCheckoutView.as_view(), name="student_buy_tests_checkout"),
    re_path(r"^student/exam/$",                                       StudentExamView.as_view(),             name="student_exam"              ),
    re_path(r"^student/exam/continue/$",                              StudentExamContinueView.as_view(),     name="student_exam_continue"     ),
    re_path(r"^student/exam/start/$",                                 StudentExamStartView.as_view(),        name="student_exam_start"        ),
    re_path(r"^student/exam/skip/$",                                  StudentExamSkipView.as_view(),         name="student_exam_skip"         ),
    re_path(r"^student/exam/end/$",                                   StudentExamEndView.as_view(),          name="student_exam_end"          ),
    re_path(r"^student/exam/report/$",                                StudentExamReportView.as_view(),       name="student_exam_report"       ),

    # DEVELOPER URLS
    re_path(r"^developer/$",                 DeveloperDashboardView.as_view(),       name="developer_dashboard"      ),
    # re_path(r"^developer/acknowledgement/$", DeveloperAcknowledgementView.as_view(), name="developer_acknowledgement"),
    re_path(r"^developer/tests/$",           DeveloperTestsView.as_view(),           name="developer_tests"          ),
    # re_path(r"^developer/questions/$",       SuperQuestionView.as_view(),            name="developer_questions"      ),
    re_path(r"^developer/offer/$",           DeveloperOfferView.as_view(),           name="developer_offer"          ),
    # re_path(r"^developer/users/$",           SuperUsersView.as_view(),               name="developer_users"          ),

    # EXPERT URLS
    re_path(r"^expert/$",                 SuperTestsView.as_view(),               name="expert_dashboard"      ),
    re_path(r"^expert/tests/$",           DeveloperTestsView.as_view(),           name="expert_tests"          ),
    re_path(r"^expert/users/$",           SuperUsersView.as_view(),               name="expert_users"          ),
    re_path(r"^expert/questions/$",       SuperQuestionView.as_view(),            name="expert_questions"      ),

    # ADMIN URLS
    re_path(r"^admin/$",                 SuperTestsView.as_view(),               name="admin_dashboard"      ),
    re_path(r"^admin/create-students/$", SuperCreateStudentsView.as_view(),      name="admin_create_students"),
    re_path(r"^admin/tests/$",           DeveloperTestsView.as_view(),           name="admin_tests"          ),
    re_path(r"^admin/users/$",           SuperUsersView.as_view(),               name="admin_users"          ),
    

    # SUPER URLS
    re_path(r"^super/$",                                        SuperDashboardView.as_view(),                name="super_dashboard"                 ),
    re_path(r"^super/tests/$",                                  SuperTestsView.as_view(),                    name="super_tests"                     ),
    re_path(r"^super/questions/$",                              SuperQuestionView.as_view(),                 name="super_questions"                 ),
    re_path(r"^super/download-subscription-list/$",             SuperDownloadSubscriptionListView.as_view(), name="super_download_subscription_list"),
    re_path(r"^super/users/$",                                  SuperUsersView.as_view(),                    name="super_users"                     ),
    re_path(r"^super/users/(?P<user_id>[0-9]+)/$",              SuperUserView.as_view(),                     name="super_user"                      ),
    re_path(r"^super/users/(?P<user_id>[0-9]+)/impersonate/$",  SuperImpersonateUserView.as_view(),          name="super_impersonate_user"          ),
    re_path(r"^super/users/(?P<user_id>[0-9]+)/give-credits/$", SuperGiveCreditsUserView.as_view(),          name="super_give_credits_user"         ),
    re_path(r"^super/users/(?P<user_id>[0-9]+)/change-pass-manual/$",   SuperChangePassManualView.as_view(),         name="super_change_pass_manual"        ),
    re_path(r"^super/users/(?P<user_id>[0-9]+)/duplicate-quizset/$",   CreateQuizSetDublicateView.as_view(),         name="super_duplicate_quizset"        ),
    re_path(r"^super/quizzes/$",                                SuperQuizzesView.as_view(),                  name="super_quizzes"                   ),
    re_path(r"^super/trial-balance/$",                          SuperTrialBalanceView.as_view(),             name="super_trial_balance"             ),
    re_path(r"^super/create-students/$",                        SuperCreateStudentsView.as_view(),           name="super_create_students"           ),
    re_path(r"^super/create-students/create-form/$",            SuperCreateStudentsFormView.as_view(),       name="super_create_students_form"      ),
    re_path(r"^super/export-data/$",                            SuperExportDataView.as_view(),               name="super_export_data"               ),
    re_path(r"^super/export-data/export-form/$",                SuperExportDataFormView.as_view(),           name="super_export_data_form"          ),
    
    # STUDENT URLS
    re_path(r"^demouser/$",                                     DemouserDashboardView.as_view(),              name="demo_dashboard"                  ),
    

    # SYSTEM URLS
    re_path(r"^login/$",                                                                            LoginView.as_view(),                name="login"                 ),
    re_path(r"^logout/$",                                                                           LogoutView.as_view(),               name="logout"                ),
    # re_path(r"^register_demo/$",                                                                    RegisterView.as_view(),             name="register"              ),
    re_path(r"^register/demo/$",                                                                   RegisterDemoUserView.as_view(),       name="register_demo"        ),
    re_path(r"^register/b2bt/$",                                                                   RegisterB2BTeacherView.as_view(),     name="register_b2bt"        ),
]
