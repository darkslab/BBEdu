from django.conf.urls import url
from .auth.views import LoginView, LogoutView, RegisterView, RegisterDeveloperView, PasswordResetView, PasswordResetConfirmView
from .views.base import (
    HomeView,
    NisView,
    NktView,
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
    url(r"^$",            HomeView.as_view(),      name="home"      ),
    url(r"^nis/$",        NisView.as_view(),       name="nis"       ),
    url(r"^nkt/$",        NktView.as_view(),       name="nkt"       ),
    url(r"^terms/$",      TermsView.as_view(),     name="terms"     ),
    url(r"^contact-us/$", ContactUsView.as_view(), name="contact_us"),
    url(r"^faq/$",        FaqView.as_view(),       name="faq"       ),

    # USER URLS
    url(r"^dashboard/$",                                       DashboardView.as_view(),               name="dashboard"                 ),
    url(r"^settings/$",                                        SettingsView.as_view(),                name="settings"                  ),
    url(r"^buy-credits/$",                                     BuyCreditsView.as_view(),              name="buy_credits"               ),
    url(r"^buy-credits-qazkom/$",                              BuyCreditsQazkomView.as_view(),        name="buy_credits_qazkom"        ),
    url(r"^buy-credits-beeline/$",                             BuyCreditsBeelineView.as_view(),       name="buy_credits_beeline"       ),
    url(r"^buy-credits-beeline/(?P<action>send|resend|pay)/$", BuyCreditsBeelineActionView.as_view(), name="buy_credits_beeline_action"),

    # UPLOAD URLS
    url(r"^uploads/start/$",                              UploadStartView.as_view(),    name="upload_start"   ),
    url(r"^uploads/(?P<uuid>[0-9A-Fa-f]{32})/complete/$", UploadCompleteView.as_view(), name="upload_complete"),
    url(r"^uploads/(?P<uuid>[0-9A-Fa-f]{32})/adopt/$",    UploadAdoptView.as_view(),    name="upload_adopt"   ),

    # TEST BUILDING URLS
    url(r"^build/tests/$",                                                                           BuildTestsView.as_view(),              name="build_tests"            ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/$",                                                BuildTestView.as_view(),               name="build_test"             ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/)?$",            BuildTestQuestionView.as_view(),       name="build_test_question"    ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/paragraphs/)?$", BuildTestParagraphsView.as_view(),     name="build_test_paragraphs"  ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/attributes/$",                                     BuildTestAttributesView.as_view(),     name="build_test_attributes"  ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/approve/$",                                        BuildApproveTestView.as_view(),        name="build_approve_test"     ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/redraft/$",                                        BuildReDraftTestView.as_view(),        name="build_redraft_test"     ), 
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/reapprove/$",                                      BuildReApproveTestView.as_view(),      name="build_reapprove_test"   ), 
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/refuse/$",                                         BuildRefuseTestView.as_view(),         name="build_refuse_test"      ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/delete/$",                                         BuildDeleteTestView.as_view(),         name="build_delete_test"      ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/toggle-free/(?P<free>true|false)/$",               BuildToggleFreeTestView.as_view(),     name="build_toggle_free_test" ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/check/$",                                          BuildCheckTestView.as_view(),          name="build_check_test"       ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview/$",                                        BuildTestPreviewView.as_view(),        name="build_test_preview"     ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview-data/$",                                   BuildTestPreviewDataView.as_view(),    name="build_test_preview_data"),

    # STUDENT URLS
    url(r"^student/$",                                         StudentDashboardView.as_view(),        name="student_dashboard"         ),
    url(r"^student/buy-tests/$",                               StudentBuyTestDomainsView.as_view(),   name="student_buy_test_domains"  ),
    url(r"^student/buy-tests/(?P<test_domain_id>7911)/$",      StudentBuyTestsViewNIS.as_view(),      name="student_buy_tests_NIS"     ),
    url(r"^student/buy-tests/(?P<test_domain_id>\d+)/$",       StudentBuyTestsView.as_view(),         name="student_buy_tests"         ),
    url(r"^student/buy-tests/(?P<test_domain_id>\d+)/cart/$",  StudentBuyTestsCartView.as_view(),     name="student_buy_tests_cart"    ),
    url(r"^student/buy-tests/checkout/$",                      StudentBuyTestsCheckoutView.as_view(), name="student_buy_tests_checkout"),
    url(r"^student/exam/$",                                    StudentExamView.as_view(),             name="student_exam"              ),
    url(r"^student/exam/continue/$",                           StudentExamContinueView.as_view(),     name="student_exam_continue"     ),
    url(r"^student/exam/start/$",                              StudentExamStartView.as_view(),        name="student_exam_start"        ),
    url(r"^student/exam/skip/$",                               StudentExamSkipView.as_view(),         name="student_exam_skip"         ),
    url(r"^student/exam/end/$",                                StudentExamEndView.as_view(),          name="student_exam_end"          ),
    url(r"^student/exam/report/$",                             StudentExamReportView.as_view(),       name="student_exam_report"       ),
    url(r"^student/results/$",                                 StudentResultsView.as_view(),          name="student_results"           ),
    url(r"^student/results/(?P<code>[0-9A-Fa-f]{4,6})/$",      StudentResultView.as_view(),           name="student_result"            ),
    url(r"^student/results/(?P<code>[0-9A-Fa-f]{4,6})/data/$", StudentResultDataView.as_view(),       name="student_result_data"       ),
    url(r"^student/transactions/$",                            StudentTransactionsView.as_view(),     name="student_transactions"      ),
    url(r"^student/transactions/(?P<transaction_id>\d+)/$",    StudentTransactionView.as_view(),      name="student_transaction"       ),

    # DEVELOPER URLS
    url(r"^developer/$",                 DeveloperDashboardView.as_view(),       name="developer_dashboard"      ),
    url(r"^developer/acknowledgement/$", DeveloperAcknowledgementView.as_view(), name="developer_acknowledgement"),
    url(r"^developer/tests/$",           DeveloperTestsView.as_view(),           name="developer_tests"          ),
    url(r"^developer/offer/$",           DeveloperOfferView.as_view(),           name="developer_offer"          ),

    # SUPER URLS
    url(r"^super/$",                                                SuperDashboardView.as_view(),                name="super_dashboard"                 ),
    url(r"^super/tests/$",                                          SuperTestsView.as_view(),                    name="super_tests"                     ),
    url(r"^super/download-subscription-list/$",                     SuperDownloadSubscriptionListView.as_view(), name="super_download_subscription_list"),
    url(r"^super/users/$",                                          SuperUsersView.as_view(),                    name="super_users"                     ),
    url(r"^super/users/(?P<user_id>[0-9]+)/$",                      SuperUserView.as_view(),                     name="super_user"                      ),
    url(r"^super/users/(?P<user_id>[0-9]+)/impersonate/$",          SuperImpersonateUserView.as_view(),          name="super_impersonate_user"          ),
    url(r"^super/users/(?P<user_id>[0-9]+)/give-credits/$",         SuperGiveCreditsUserView.as_view(),          name="super_give_credits_user"         ),
    url(r"^super/users/(?P<user_id>[0-9]+)/change-pass-manual/$",   SuperChangePassManualView.as_view(),         name="super_change_pass_manual"        ),
    url(r"^super/quizzes/$",                                        SuperQuizzesView.as_view(),                  name="super_quizzes"                   ),
    url(r"^super/trial-balance/$",                                  SuperTrialBalanceView.as_view(),             name="super_trial_balance"             ),
    url(r"^super/export-data/$",                                    SuperExportDataView.as_view(),               name="super_export_data"               ),
    url(r"^super/export-data/export-form/$",                        SuperExportDataFormView.as_view(),           name="super_export_data_form"          ),
    url(r"^super/change-price/$",                                   SuperChangePriceView.as_view(),              name="super_change_price"              ),


    # SYSTEM URLS
    url(r"^login/$",                                                                            LoginView.as_view(),                name="login"                 ),
    url(r"^logout/$",                                                                           LogoutView.as_view(),               name="logout"                ),
    url(r"^register/$",                                                                         RegisterView.as_view(),             name="register"              ),
    url(r"^register/developer/$",                                                               RegisterDeveloperView.as_view(),    name="register_developer"    ),
    url(r"^password-reset/$",                                                                   PasswordResetView.as_view(),        name="password_reset"        ),
    url(r"^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]
