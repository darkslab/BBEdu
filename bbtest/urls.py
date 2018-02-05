from django.conf.urls import url
from .auth.views import LoginView, LogoutView, RegisterView, PasswordResetView, PasswordResetConfirmView
from .views import (
    HomeView, DashboardView, SettingsView,
    UploadStartView, UploadCompleteView, UploadAdoptView,
)
from .views.student import DashboardView as StudentDashboardView
from .views.developer import (
    DashboardView as DeveloperDashboardView,
    AcknowledgementView,
    TestsView,
    TestView,
    TestPreviewView,
    TestPreviewDataView,
    TestDeleteView,
    QuestionView,
    ParagraphsView,
    AttributesView,
)
from .views.super import DashboardView as SuperDashboardView


app_name = "bbtest"
urlpatterns = [
    # PUBLIC URLS
    url(r"^$", HomeView.as_view(), name="home"),

    # USER URLS
    url(r"^dashboard/$", DashboardView.as_view(), name="dashboard"),
    url(r"^settings/$", SettingsView.as_view(), name="settings"),

    # UPLOAD URLS
    url(r"^uploads/start/$", UploadStartView.as_view(), name="upload_start"),
    url(r"^uploads/(?P<uuid>[0-9A-Fa-f]{32})/complete/$", UploadCompleteView.as_view(), name="upload_complete"),
    url(r"^uploads/(?P<uuid>[0-9A-Fa-f]{32})/adopt/$", UploadAdoptView.as_view(), name="upload_adopt"),

    # STUDENT URLS
    url(r"^student/$", StudentDashboardView.as_view(), name="student_dashboard"),

    # DEVELOPER URLS
    url(r"^developer/$", DeveloperDashboardView.as_view(), name="developer_dashboard"),
    url(r"^developer/acknowledgement/$", AcknowledgementView.as_view(), name="developer_acknowledgement"),
    url(r"^developer/tests/$", TestsView.as_view(), name="developer_tests"),
    url(r"^developer/tests/(?P<code>[0-9A-Fa-f]{4,6})/$", TestView.as_view(), name="developer_test"),
    url(r"^developer/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview/$", TestPreviewView.as_view(), name="developer_preview_test"),
    url(r"^developer/tests/(?P<code>[0-9A-Fa-f]{4,6})/preview-data/$", TestPreviewDataView.as_view(), name="developer_preview_data_test"),
    url(r"^developer/tests/(?P<code>[0-9A-Fa-f]{4,6})/delete/$", TestDeleteView.as_view(), name="developer_delete_test"),
    url(r"^developer/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/)?$", QuestionView.as_view(), name="developer_question"),
    url(r"^developer/tests/(?P<code>[0-9A-Fa-f]{4,6})/questions/(?:(?P<question_id>\d+)/paragraphs/)?$", ParagraphsView.as_view(), name="developer_paragraphs"),
    url(r"^developer/tests/(?P<code>[0-9A-Fa-f]{4,6})/attributes/$", AttributesView.as_view(), name="developer_attributes"),

    # SUPER URLS
    url(r"^super/$", SuperDashboardView.as_view(), name="super_dashboard"),

    # SYSTEM URLS
    url(r"^login/$", LoginView.as_view(), name="login"),
    url(r"^logout/$", LogoutView.as_view(), name="logout"),
    url(r"^register/(?:(?P<group>developer)/)?$", RegisterView.as_view(), name="register"),
    url(r"^password-reset/$", PasswordResetView.as_view(), name="password_reset"),
    url(r"^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]


# from django.views.generic import TemplateView
# urlpatterns += [
#     url(r"^page/$", TemplateView.as_view(template_name="page.html"), {
#         "var": 1,
#     }),
# ]
