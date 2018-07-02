# -*- coding: utf-8 -*-
try:
    from django.conf.urls.defaults import *
except ImportError:
    from django.conf.urls import re_path, include

from django.contrib import admin
admin.autodiscover()

from report_creator import report
report.autodiscover()


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('report_creator.urls')),
]
