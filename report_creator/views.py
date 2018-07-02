# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from report_creator.report import reports

from django.shortcuts import render


def report_list(request):
    """
    This view render all reports registered
    """
    #for report in reports.get_reports():
    #    print(report.get_title(report))

    context = {
        'report_list': reports.get_reports()
    }

    return render(request, 'report_creator/report_list.html', context)
    #context_instance=RequestContext(request)

def report(request, slug):
    """
    This view render one report

    Keywords arguments:

    slug -- slug of the report
    """
    report_class = reports.get_report(slug)
    if not report_class:
        raise Http404
    context = {
        'report_list': reports.get_reports()
    }

    report = report_class(request=request)
    return report.render(request, extra_context=context)
