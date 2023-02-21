from django.urls import re_path
from .auth.views import LoginView, LogoutView, RegisterView, RegisterDeveloperView, PasswordResetView, PasswordResetConfirmView
from .views.base import (
    HomeView,
    NisView,
    NktView,
    NktView2,
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
    ToggleFreeTestView   as BuildToggleFreeTestView,
    CheckTestView        as BuildCheckTestView,
    TestPreviewView      as BuildTestPreviewView,
    TestPreviewDataView  as BuildTestPreviewDataView,
)
from .views.student import (
    DashboardView         as StudentDashboardView,
    BuyTestDomainsView    as StudentBuyTestDomainsView,
    BuyTestsView          as StudentBuyTestsView,
    BuyTestsViewNIS       as StudentBuyTestsViewNIS,
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
from .views.developer import (
    DashboardView        as DeveloperDashboardView,
    AcknowledgementView  as DeveloperAcknowledgementView,
    TestsView            as DeveloperTestsView,
    OfferView            as DeveloperOfferView,
)
from .views.super import (
    DashboardView                 as SuperDashboardView,
    TestsView                     as SuperTestsView,
    DownloadSubscriptionListView  as SuperDownloadSubscriptionListView,
    UsersView                     as SuperUsersView,
    UserView                      as SuperUserView,
    ImpersonateUserView           as SuperImpersonateUserView,
    GiveCreditsUserView           as SuperGiveCreditsUserView,
    ChangePassManualView          as SuperChangePassManualView,
    QuizzesView                   as SuperQuizzesView,
    TrialBalanceView              as SuperTrialBalanceView,
    ExportDataView                as SuperExportDataView,
    ExportDataFormView            as SuperExportDataFormView,
    ChangePriceView               as SuperChangePriceView,
)


app_name = "bbtest"
urlpatterns = [
    # PUBLIC URLS
    re_path(r"^$",            HomeView.as_view(),      name="home"      ),
    re_path(r"^nis/$",        NisView.as_view(),       name="nis"       ),
    # re_path(r"^asd/$",        NktView.as_view(),       name="nkt"       ),
    re_path(r"^nkt/$",        NktView.as_view(),      name="nkt"       ),
    re_path(r"^terms/$",      TermsView.as_view(),     name="terms"     ),
    re_path(r"^contact-us/$", ContactUsView.as_view(), name="contact_us"),
    re_path(r"^faq/$",        FaqView.as_view(),       name="faq"       ),

    # USER URLS
    re_path(r"^dashboard/$",                                       DashboardView.as_view(),               name="dashboard"                 ),
    re_path(r"^settings/$",                                        SettingsView.as_view(),                name="settings"                  ),
    re_path(r"^buy-credits/$",                                     BuyCreditsView.as_view(),              name="buy_credits"               ),
    re_path(r"^buy-credits-qazkom/$",                              BuyCreditsQazkomView.as_view(),        name="buy_credits_qazkom"        ),
    re_path(r"^buy-credits-beeline/$",                             BuyCreditsBeelineView.as_view(),       name="buy_credits_beeline"       ),
    re_path(r"^buy-credits-beeline/(?P<action>send|resend|pay)/$", BuyCreditsBeelineActionView.as_view(), name="buy_credits_beeline_action"),

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
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/refuse/$",                                         BuildRefuseTestView.as_view(),         name="build_refuse_test"      ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/delete/$",                                         BuildDeleteTestView.as_view(),         name="build_delete_test"      ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/toggle-free/(?P<free>true|false)/$",               BuildToggleFreeTestView.as_view(),     name="build_toggle_free_test" ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/check/$",                                          BuildCheckTestView.as_view(),          name="build_check_test"       ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview/$",                                        BuildTestPreviewView.as_view(),        name="build_test_preview"     ),
    re_path(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview-data/$",                                   BuildTestPreviewDataView.as_view(),    name="build_test_preview_data"),

    # STUDENT URLS
    re_path(r"^student/$",                                         StudentDashboardView.as_view(),        name="student_dashboard"         ),
    re_path(r"^student/buy-tests/$",                               StudentBuyTestDomainsView.as_view(),   name="student_buy_test_domains"  ),
    re_path(r"^student/buy-tests/(?P<test_domain_id>7911)/$",      StudentBuyTestsViewNIS.as_view(),      name="student_buy_tests_NIS"     ),
    re_path(r"^student/buy-tests/(?P<test_domain_id>\d+)/$",       StudentBuyTestsView.as_view(),         name="student_buy_tests"         ),
    re_path(r"^student/buy-tests/(?P<test_domain_id>\d+)/cart/$",  StudentBuyTestsCartView.as_view(),     name="student_buy_tests_cart"    ),
    re_path(r"^student/buy-tests/checkout/$",                      StudentBuyTestsCheckoutView.as_view(), name="student_buy_tests_checkout"),
    re_path(r"^student/exam/$",                                    StudentExamView.as_view(),             name="student_exam"              ),
    re_path(r"^student/exam/continue/$",                           StudentExamContinueView.as_view(),     name="student_exam_continue"     ),
    re_path(r"^student/exam/start/$",                              StudentExamStartView.as_view(),        name="student_exam_start"        ),
    re_path(r"^student/exam/skip/$",                               StudentExamSkipView.as_view(),         name="student_exam_skip"         ),
    re_path(r"^student/exam/end/$",                                StudentExamEndView.as_view(),          name="student_exam_end"          ),
    re_path(r"^student/exam/report/$",                             StudentExamReportView.as_view(),       name="student_exam_report"       ),
    re_path(r"^student/results/$",                                 StudentResultsView.as_view(),          name="student_results"           ),
    re_path(r"^student/results/(?P<code>[0-9A-Fa-f]{4,6})/$",      StudentResultView.as_view(),           name="student_result"            ),
    re_path(r"^student/results/(?P<code>[0-9A-Fa-f]{4,6})/data/$", StudentResultDataView.as_view(),       name="student_result_data"       ),
    re_path(r"^student/transactions/$",                            StudentTransactionsView.as_view(),     name="student_transactions"      ),
    re_path(r"^student/transactions/(?P<transaction_id>\d+)/$",    StudentTransactionView.as_view(),      name="student_transaction"       ),

    # DEVELOPER URLS
    re_path(r"^developer/$",                 DeveloperDashboardView.as_view(),       name="developer_dashboard"      ),
    re_path(r"^developer/acknowledgement/$", DeveloperAcknowledgementView.as_view(), name="developer_acknowledgement"),
    re_path(r"^developer/tests/$",           DeveloperTestsView.as_view(),           name="developer_tests"          ),
    re_path(r"^developer/offer/$",           DeveloperOfferView.as_view(),           name="developer_offer"          ),

    # SUPER URLS
    re_path(r"^super/$",                                                SuperDashboardView.as_view(),                name="super_dashboard"                 ),
    re_path(r"^super/tests/$",                                          SuperTestsView.as_view(),                    name="super_tests"                     ),
    re_path(r"^super/download-subscription-list/$",                     SuperDownloadSubscriptionListView.as_view(), name="super_download_subscription_list"),
    re_path(r"^super/users/$",                                          SuperUsersView.as_view(),                    name="super_users"                     ),
    re_path(r"^super/users/(?P<user_id>[0-9]+)/$",                      SuperUserView.as_view(),                     name="super_user"                      ),
    re_path(r"^super/users/(?P<user_id>[0-9]+)/impersonate/$",          SuperImpersonateUserView.as_view(),          name="super_impersonate_user"          ),
    re_path(r"^super/users/(?P<user_id>[0-9]+)/give-credits/$",         SuperGiveCreditsUserView.as_view(),          name="super_give_credits_user"         ),
    re_path(r"^super/users/(?P<user_id>[0-9]+)/change-pass-manual/$",   SuperChangePassManualView.as_view(),         name="super_change_pass_manual"        ),
    re_path(r"^super/quizzes/$",                                        SuperQuizzesView.as_view(),                  name="super_quizzes"                   ),
    re_path(r"^super/trial-balance/$",                                  SuperTrialBalanceView.as_view(),             name="super_trial_balance"             ),
    re_path(r"^super/export-data/$",                                    SuperExportDataView.as_view(),               name="super_export_data"               ),
    re_path(r"^super/export-data/export-form/$",                        SuperExportDataFormView.as_view(),           name="super_export_data_form"          ),
    re_path(r"^super/change-price/$",                                   SuperChangePriceView.as_view(),              name="super_change_price"              ),


    # SYSTEM URLS
    re_path(r"^login/$",                                                                            LoginView.as_view(),                name="login"                 ),
    re_path(r"^logout/$",                                                                           LogoutView.as_view(),               name="logout"                ),
    re_path(r"^register/$",                                                                         RegisterView.as_view(),             name="register"              ),
    re_path(r"^register/developer/$",                                                               RegisterDeveloperView.as_view(),    name="register_developer"    ),
    re_path(r"^password-reset/$",                                                                   PasswordResetView.as_view(),        name="password_reset"        ),
    re_path(r"^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]
