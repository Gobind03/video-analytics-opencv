"""WifiberAnalyticsWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from accounts import urls as accounts_urls
from cam_registry import urls as cam_registry_urls
from landing_site import urls as landing_site_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls)),
    path('cam-registry/', include(cam_registry_urls)),
    path('landing/', include(landing_site_urls)),
    path('', lambda r: HttpResponseRedirect('landing/home/')),
]
