from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from .auth.forms import AuthenticationForm
from .views import HomeView, TestView


app_name = "bbtest"
urlpatterns = [
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^test/$", TestView.as_view(), name="test"),

    url(r"^login/$", LoginView.as_view(
        template_name="login.html",
        redirect_field_name=settings.BB_REDIRECT_FIELDNAME,
        authentication_form=AuthenticationForm,
        redirect_authenticated_user=True,
    ), name="login"),
    url(r"^logout/$", LogoutView.as_view(
        redirect_field_name=settings.BB_REDIRECT_FIELDNAME,
    ), name="logout"),
]
