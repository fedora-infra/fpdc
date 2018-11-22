"""fpdc URL Configuration

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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from fpdc.releases.views import ReleaseViewSet

schemaview = get_schema_view(title="Fedora Product Definition Center", url=settings.COREAPI_URL)

router = DefaultRouter(trailing_slash=False)

router.register(r"release", ReleaseViewSet)

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^oidc/", include("mozilla_django_oidc.urls")),
    url(r"^api/v1/", include((router.urls, "releases"), namespace="v1")),
    url(r"^docs/", include_docs_urls(title="Fedora Product Definition Center")),
    url(r"^$", schemaview),
]
