 


Django Report Creator
===================

django-report-creator is a Django application and library for reports integrated with highcharts.


[![Build Status](https://travis-ci.org/bytcode/django-report-creator.png)](https://travis-ci.org/bytcode/django-report-creator)

--------------------------------------------------------------------


Documentation
=============

https://django-report-creator.readthedocs.org/en/latest/

ForeignKey queryset in main report.py file:

    list_filter_queryset = {
        'user': {'groups__in': [13, 34]},
    }

Custom widget:

    list_filter_widget = {
        'state':  SelectMultiple(),
    }

Contribute
==========

Clone the repo and help to be better this app :)

