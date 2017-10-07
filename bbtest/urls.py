from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from .auth.forms import AuthenticationForm
from .auth.views import RegisterView
from .views import HomeView
from .views.developer import DeveloperDashboardView


app_name = "bbtest"
urlpatterns = [
    # PUBLIC URLS
    url(r"^$", HomeView.as_view(), name="home"),

    # DEVELOPER URLS
    url(r"^developer/$", DeveloperDashboardView.as_view(), name="developer_dashboard"),

    # SYSTEM URLS
    url(r"^login/$", LoginView.as_view(
        template_name="login.html",
        redirect_field_name=settings.BB_REDIRECT_FIELDNAME,
        authentication_form=AuthenticationForm,
        redirect_authenticated_user=True,
    ), name="login"),
    url(r"^logout/$", LogoutView.as_view(
        redirect_field_name=settings.BB_REDIRECT_FIELDNAME,
    ), name="logout"),
    url(r"^register/(?:(?P<group>developer)/)?$", RegisterView.as_view(), name="register"),
]
