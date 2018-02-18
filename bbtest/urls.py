from django.conf.urls import url
from .auth.views import LoginView, LogoutView, RegisterView, PasswordResetView, PasswordResetConfirmView
from .views.base import HomeView, DashboardView, SettingsView
from .views.upload import UploadStartView, UploadCompleteView, UploadAdoptView
from .views.test import (
    TestView as BuildTestView,
    TestQuestionView as BuildTestQuestionView,
    TestParagraphsView as BuildTestParagraphsView,
    TestAttributesView as BuildTestAttributesView,
    ApproveTestView as BuildApproveTestView,
    RefuseTestView as BuildRefuseTestView,
    DeleteTestView as BuildDeleteTestView,
    TestPreviewView as BuildTestPreviewView,
    TestPreviewDataView as BuildTestPreviewDataView,
)
from .views.student import (
    DashboardView as StudentDashboardView,
)
from .views.developer import (
    DashboardView as DeveloperDashboardView,
    AcknowledgementView as DeveloperAcknowledgementView,
    TestsView as DeveloperTestsView,
)
from .views.super import (
    DashboardView as SuperDashboardView,
    TestsView as SuperTestsView,
)


app_name = "bbtest"
urlpatterns = [
    # PUBLIC URLS
    url(r"^$", HomeView.as_view(), name="home"),

    # USER URLS
    url(r"^dashboard/$", DashboardView.as_view(), name="dashboard"),
    url(r"^settings/$",  SettingsView.as_view(),  name="settings" ),

    # UPLOAD URLS
    url(r"^uploads/start/$",                              UploadStartView.as_view(),    name="upload_start"   ),
    url(r"^uploads/(?P<uuid>[0-9A-Fa-f]{32})/complete/$", UploadCompleteView.as_view(), name="upload_complete"),
    url(r"^uploads/(?P<uuid>[0-9A-Fa-f]{32})/adopt/$",    UploadAdoptView.as_view(),    name="upload_adopt"   ),

    # TEST BUILDING URLS
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/$",                                                BuildTestView.as_view(),               name="build_test"             ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/)?$",            BuildTestQuestionView.as_view(),       name="build_test_question"    ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/paragraphs/)?$", BuildTestParagraphsView.as_view(),     name="build_test_paragraphs"  ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/attributes/$",                                     BuildTestAttributesView.as_view(),     name="build_test_attributes"  ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/approve/$",                                        BuildApproveTestView.as_view(),        name="build_approve_test"     ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/refuse/$",                                         BuildRefuseTestView.as_view(),         name="build_refuse_test"      ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/delete/$",                                         BuildDeleteTestView.as_view(),         name="build_delete_test"      ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview/$",                                        BuildTestPreviewView.as_view(),        name="build_test_preview"     ),
    url(r"^build/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview-data/$",                                   BuildTestPreviewDataView.as_view(),    name="build_test_preview_data"),

    # STUDENT URLS
    url(r"^student/$", StudentDashboardView.as_view(), name="student_dashboard"),

    # DEVELOPER URLS
    url(r"^developer/$",                 DeveloperDashboardView.as_view(),       name="developer_dashboard"      ),
    url(r"^developer/acknowledgement/$", DeveloperAcknowledgementView.as_view(), name="developer_acknowledgement"),
    url(r"^developer/tests/$",           DeveloperTestsView.as_view(),           name="developer_tests"          ),

    # SUPER URLS
    url(r"^super/$",                                                                                 SuperDashboardView.as_view(),       name="super_dashboard"        ),
    url(r"^super/tests/$",                                                                           SuperTestsView.as_view(),           name="super_tests"            ),
    # url(r"^super/tests/(?P<code>[0-9A-Fa-f]{4,6})/$",                                                SuperTestView.as_view(),            name="super_test"             ),
    # url(r"^super/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/)?$",            SuperQuestionView.as_view(),        name="super_question"         ),
    # url(r"^super/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/paragraphs/)?$", SuperParagraphsView.as_view(),      name="super_paragraphs"       ),
    # url(r"^super/tests/(?P<code>[0-9A-Fa-f]{4,6})/attributes/$",                                     SuperAttributesView.as_view(),      name="super_attributes"       ),
    # url(r"^super/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview/$",                                        SuperTestPreviewView.as_view(),     name="super_preview_test"     ),
    # url(r"^super/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview-data/$",                                   SuperTestPreviewDataView.as_view(), name="super_preview_data_test"),
    # url(r"^super/tests/(?P<code>[0-9A-Fa-f]{4,6})/approve/$",                                        ApproveTestView.as_view(),          name="super_approve_test"     ),
    # url(r"^super/tests/(?P<code>[0-9A-Fa-f]{4,6})/refuse/$",                                         RefuseTestView.as_view(),           name="super_refuse_test"      ),

    # SYSTEM URLS
    url(r"^login/$",                                                                            LoginView.as_view(),                name="login"                 ),
    url(r"^logout/$",                                                                           LogoutView.as_view(),               name="logout"                ),
    url(r"^register/(?:(?P<group>developer)/)?$",                                               RegisterView.as_view(),             name="register"              ),
    url(r"^password-reset/$",                                                                   PasswordResetView.as_view(),        name="password_reset"        ),
    url(r"^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]


# from django.views.generic import TemplateView
# urlpatterns += [
#     url(r"^page/$", TemplateView.as_view(template_name="page.html"), {
#         "var": 1,
#     }),
# ]
