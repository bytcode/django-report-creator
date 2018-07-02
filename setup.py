# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages


version = __import__('report_creator').__version__


LONG_DESCRIPTION = """
django-report-creator
===================

django reports integrated with highcharts

    $ git clone git://github.com/bytcode/django-report-creator.git
"""


def long_description():
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-report-creator',
      version=version,
      author='Joseph M. Daudi',
      author_email='joseph@bytcode.com',
      description='Django reports integrated with highcharts.',
      license='BSD',
      keywords='django, report, reports, report-creator, highcharts, generator with model',
      url='https://github.com/bytcode/django-report-creator',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      long_description=long_description(),
      install_requires=[
        'django>=1.3',
        'reportlab',
        'html5lib',
        'BeautifulSoup',
        'xhtml2pdf',
        'xlwt',
      ],
      classifiers=['Framework :: Django',
                   'Development Status :: 3 - Alpha',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 3'])
