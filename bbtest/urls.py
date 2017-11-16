from django.conf.urls import url
from .auth.views import LoginView, LogoutView, RegisterView
from .views import HomeView
from .views.student import DashboardView as StudentDashboardView
from .views.developer import DashboardView as DeveloperDashboardView


app_name = "bbtest"
urlpatterns = [
    # PUBLIC URLS
    url(r"^$", HomeView.as_view(), name="home"),

    # DEVELOPER URLS
    url(r"^student/$", StudentDashboardView.as_view(), name="student_dashboard"),
    url(r"^developer/$", DeveloperDashboardView.as_view(), name="developer_dashboard"),

    # SYSTEM URLS
    url(r"^login/$", LoginView.as_view(), name="login"),
    url(r"^logout/$", LogoutView.as_view(), name="logout"),
    url(r"^register/(?:(?P<group>developer)/)?$", RegisterView.as_view(), name="register"),
]
