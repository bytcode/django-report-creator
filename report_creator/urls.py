# -*- coding: utf-8 -*-
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls import *
from django.urls import re_path

from report_creator.views import report, report_list


urlpatterns = [
    re_path(r'^$', report_list, name='model_report_list'),
    re_path(r'^(?P<slug>[\w-]+)/$', report, name='model_report_view'),
]
