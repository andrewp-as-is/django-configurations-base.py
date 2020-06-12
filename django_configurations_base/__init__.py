import os

from configurations import values
from django_configurations_apps import AppsConfiguration
from django_configurations_templates import TemplatesConfiguration

def getlist(path):
    return list(filter(
        None,map(lambda s:s.strip(),open(path).read().splitlines() if path else [])
    ))

class BaseConfiguration(AppsConfiguration,TemplatesConfiguration):
    ALLOWED_HOSTS = values.ListValue([])
    AUTHENTICATION_BACKENDS = values.ListValue(['django.contrib.auth.backends.ModelBackend'])
    AUTH_USER_MODEL = values.Value('auth.User')
    BASE_DIR = os.getcwd()
    DEBUG = bool(os.getenv('DJANGO_DEBUG','').lower() in ('yes', 'y', 'true', '1'))
    INTERNAL_IPS = values.ListValue([])
    LANGUAGE_CODE = values.Value('en-us')
    LOGIN_REDIRECT_URL = values.Value('/')
    LOGOUT_REDIRECT_URL = values.Value('/')
    MEDIA_ROOT = values.Value(None)
    MEDIA_URL = '/media/'
    MIDDLEWARE = values.ListValue([])
    MIDDLEWARE_FILE = values.Value(None)
    ROOT_URLCONF = values.Value(None)
    SITE_ID = values.IntegerValue(None)
    STATIC_ROOT = values.Value(None)
    STATIC_URL = '/static/'
    STATICFILES_DIRS = values.ListValue([])
    SECRET_KEY = values.SecretValue()
    WSGI_APPLICATION = 'wsgi.application'

    @classmethod
    def pre_setup(cls):
        super(BaseConfiguration, cls).pre_setup()
        if cls.DEBUG:
            cls.ALLOWED_HOSTS = ['*']
        if not hasattr(cls,'MEDIA_ROOT') or not cls.MEDIA_ROOT:
            cls.MEDIA_ROOT = os.path.join(cls.BASE_DIR, 'media')
        if not hasattr(cls,'STATIC_ROOT') or not cls.STATIC_ROOT:
            cls.STATIC_ROOT = os.path.join(cls.BASE_DIR, 'static')
        if not hasattr(cls,'STATICFILES_DIRS') or not cls.STATICFILES_DIRS:
            path = os.path.join(cls.BASE_DIR, 'assets')
            if os.path.exists(path):
                cls.STATICFILES_DIRS = (
                    path,
                )
        if not cls.DATABASES and 'DJANGO_DATABASE_URL' in os.environ:
            cls.DATABASES = values.DatabaseURLValue(default=os.environ['DJANGO_DATABASE_URL'])
        if not hasattr(cls,'ROOT_URLCONF') or not cls.ROOT_URLCONF:
            for filename in ['urls','urls.py']:
                if os.path.exists(os.path.join(cls.BASE_DIR, filename)):
                    cls.ROOT_URLCONF = 'urls'

    @classmethod
    def setup(cls):
        super(BaseConfiguration, cls).setup()
        for middleware in getlist(cls.MIDDLEWARE_FILE):
            if middleware not in cls.MIDDLEWARE:
                cls.MIDDLEWARE.append(middleware)
