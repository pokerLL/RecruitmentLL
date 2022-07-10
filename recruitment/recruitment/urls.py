"""recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include

from django.utils.translation import gettext_lazy as _


urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')), #国际化
    path('api-auth/', include('rest_framework.urls')), # DRF AUTH
    path('api/', include('jobs.urls')), # DRF API
]

admin.site.site_header = _('匠果科技招聘管理系统')