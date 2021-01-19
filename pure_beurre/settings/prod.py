# Custom settings for the production environment

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# When DEBUG is False and a view raises an exception, all information
# will be sent by email to the people listed in the ADMINS setting
ADMINS = (('ulrichy', 'rekinvector@gmail.com'), )

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pure_beurre',
        'USER': 'v3ct0r22',
        'PASSWORD': 'V3ct0r22*',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Production statics files #

# Static files settings
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, '/static'), )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# dj-database-url configuration
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)