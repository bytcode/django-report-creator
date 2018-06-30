# -*- coding: utf-8 -*-
import io as StringIO
from io import BytesIO
from cgi import escape
from xhtml2pdf import pisa
from django.utils.encoding import force_text

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.template.loader import render_to_string
from .base import Exporter
from django.template.loader import render_to_string

class PdfExporter(Exporter):

    @classmethod
    def render(cls, report, column_labels, report_rows, report_inlines):
        # where is_export is being used?
        setattr(report, 'is_export', True)
        context_dict = {
            'report': report,
            'column_labels': column_labels,
            'report_rows': report_rows,
            'report_inlines': report_inlines,
            'pagesize': 'legal landscape'
        }

        template = get_template('model_report/export_pdf.html')
        #template = get_template(path)
        html = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

        #html = render_to_string('model_report/export_pdf.html', context_dict)
        #html = str(html)
        #print(type(html))


        # context = Context(context_dict)
        # html = template.render(context)
        #result = StringIO.StringIO()
        pdf_encoding = 'UTF-8'


        #pdf = pisa.CreatePDF(html.encode('utf-8'), result, encoding='utf-8')

        if not pdf.err:
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s.pdf' % report.slug
        else:
            response = HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

        result.close()
        return response
