from django.conf.urls import url
from .auth.views import LoginView, LogoutView, RegisterView, PasswordResetView, PasswordResetConfirmView
from .views import HomeView, DashboardView
from .views.student import DashboardView as StudentDashboardView
from .views.developer import DashboardView as DeveloperDashboardView


app_name = "bbtest"
urlpatterns = [
    # PUBLIC URLS
    url(r"^$", HomeView.as_view(), name="home"),

    # USER URLS
    url(r"^dashboard/$", DashboardView.as_view(), name="dashboard"),

    # STUDENT URLS
    url(r"^student/$", StudentDashboardView.as_view(), name="student_dashboard"),

    # DEVELOPER URLS
    url(r"^developer/$", DeveloperDashboardView.as_view(), name="developer_dashboard"),

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
