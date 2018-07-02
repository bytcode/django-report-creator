from django.conf import settings

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': settings.PROJECT_ABSOLUTE_DIR + '/report_creator.db',                      # Or path to database file if using sqlite3.
     }
 }
