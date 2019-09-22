"""bbedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from bbtest.views.generic import TemplateView
from bbtest.views.base import ProcessCreditsQazkomView


urlpatterns = [
    url(r"^robots\.txt$", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots"),
    url(r"^sitemap\.xml$", TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"), name="sitemap"),

    url(r"^process-credits-qazkom/$", ProcessCreditsQazkomView.as_view(), name="process_credits_qazkom"),
]
urlpatterns += i18n_patterns(url(r"^", include("bbtest.urls")))
