import os

from django.conf.global_settings import *
from configurations import Configuration, values


class BaseConfiguration(Configuration):
    BASE_DIR = os.getcwd()
    ROOT_URLCONF = values.Value(None)
    SITE_ID = values.IntegerValue(None)

    # CORE
    DEBUG = values.BooleanValue(DEBUG)
    DEBUG_PROPAGATE_EXCEPTIONS = values.BooleanValue(
        DEBUG_PROPAGATE_EXCEPTIONS)
    INTERNAL_IPS = values.ListValue(INTERNAL_IPS)
    ALLOWED_HOSTS = values.ListValue(ALLOWED_HOSTS)
    TIME_ZONE = values.Value(TIME_ZONE)
    USE_TZ = values.Value(USE_TZ)
    LANGUAGE_CODE = values.Value(LANGUAGE_CODE)
    LANGUAGES_BIDI = values.Value(LANGUAGES_BIDI)
    USE_I18N = values.Value(USE_I18N)
    LOCALE_PATHS = values.ListValue([])
    USE_L10N = values.Value(USE_L10N)
    DEFAULT_CHARSET = values.Value(DEFAULT_CHARSET)
    SERVER_EMAIL = values.Value(SERVER_EMAIL)
    DATABASE_ROUTERS = values.Value(DATABASE_ROUTERS)
    EMAIL_BACKEND = values.Value(EMAIL_BACKEND)
    EMAIL_HOST = values.Value(EMAIL_HOST)
    EMAIL_PORT = values.IntegerValue(EMAIL_PORT)

    INSTALLED_APPS = values.ListValue(INSTALLED_APPS)
    FORM_RENDERER = values.Value(FORM_RENDERER)
    DISALLOWED_USER_AGENTS = values.Value(DISALLOWED_USER_AGENTS)
    IGNORABLE_404_URLS = values.Value(IGNORABLE_404_URLS)
    SECRET_KEY = values.SecretValue(None)
    DEFAULT_FILE_STORAGE = values.Value(DEFAULT_FILE_STORAGE)
    MEDIA_ROOT = values.Value(MEDIA_ROOT)
    MEDIA_URL = values.Value(MEDIA_URL)
    STATIC_ROOT = values.Value(STATIC_ROOT)
    STATIC_URL = values.Value(STATIC_URL)
    FILE_UPLOAD_HANDLERS = values.ListValue(FILE_UPLOAD_HANDLERS)
    FILE_UPLOAD_MAX_MEMORY_SIZE = values.IntegerValue(
        FILE_UPLOAD_MAX_MEMORY_SIZE)
    DATA_UPLOAD_MAX_MEMORY_SIZE = values.IntegerValue(
        DATA_UPLOAD_MAX_MEMORY_SIZE)
    DATA_UPLOAD_MAX_NUMBER_FIELDS = values.IntegerValue(
        DATA_UPLOAD_MAX_NUMBER_FIELDS)
    FILE_UPLOAD_TEMP_DIR = values.Value(FILE_UPLOAD_TEMP_DIR)

    STATICFILES_DIRS = values.ListValue([])

    WSGI_APPLICATION = values.Value(WSGI_APPLICATION)

    # MIDDLEWARE
    MIDDLEWARE = values.ListValue([])

    # AUTHENTICATION
    AUTH_USER_MODEL = values.Value(AUTH_USER_MODEL)
    AUTHENTICATION_BACKENDS = values.ListValue(AUTHENTICATION_BACKENDS)
    LOGIN_URL = values.Value(LOGIN_URL)
    LOGIN_REDIRECT_URL = values.Value(LOGIN_URL)
    LOGOUT_REDIRECT_URL = values.Value(LOGOUT_REDIRECT_URL)
    PASSWORD_RESET_TIMEOUT_DAYS = values.IntegerValue(
        PASSWORD_RESET_TIMEOUT_DAYS)
    PASSWORD_RESET_TIMEOUT = values.IntegerValue(PASSWORD_RESET_TIMEOUT)
    PASSWORD_HASHERS = values.ListValue(PASSWORD_HASHERS)
    AUTH_PASSWORD_VALIDATORS = values.ListValue(AUTH_PASSWORD_VALIDATORS)

    # SIGNING
    SIGNING_BACKEND = values.Value(SIGNING_BACKEND)

    # CSRF
    CSRF_FAILURE_VIEW = values.Value(CSRF_FAILURE_VIEW)
    CSRF_COOKIE_NAME = values.Value(CSRF_COOKIE_NAME)
    CSRF_COOKIE_AGE = values.IntegerValue(CSRF_COOKIE_AGE)
    CSRF_COOKIE_DOMAIN = values.Value(CSRF_COOKIE_DOMAIN)
    CSRF_COOKIE_PATH = values.Value(CSRF_COOKIE_PATH)
    CSRF_COOKIE_SECURE = values.BooleanValue(CSRF_COOKIE_SECURE)
    CSRF_COOKIE_HTTPONLY = values.BooleanValue(CSRF_COOKIE_SECURE)
    CSRF_COOKIE_SAMESITE = values.Value(CSRF_COOKIE_SAMESITE)
    CSRF_HEADER_NAME = values.Value(CSRF_HEADER_NAME)
    CSRF_TRUSTED_ORIGINS = values.ListValue(CSRF_TRUSTED_ORIGINS)
    CSRF_USE_SESSIONS = values.BooleanValue(CSRF_USE_SESSIONS)

    # MESSAGES
    MESSAGE_STORAGE = values.Value(MESSAGE_STORAGE)

    # LOGGING
    LOGGING_CONFIG = values.Value(LOGGING_CONFIG)
    DEFAULT_EXCEPTION_REPORTER = values.Value(DEFAULT_EXCEPTION_REPORTER)
    DEFAULT_EXCEPTION_REPORTER_FILTER = values.Value(
        DEFAULT_EXCEPTION_REPORTER_FILTER)

    # TESTING
    TEST_RUNNER = values.Value(TEST_RUNNER)
    TEST_NON_SERIALIZED_APPS = values.ListValue(TEST_NON_SERIALIZED_APPS)

    # FIXTURES
    FIXTURE_DIRS = values.ListValue(FIXTURE_DIRS)

    # STATICFILES
    STATICFILES_DIRS = values.ListValue(STATICFILES_DIRS)
    STATICFILES_STORAGE = values.Value(STATICFILES_STORAGE)
    STATICFILES_FINDERS = values.ListValue(STATICFILES_FINDERS)

    # SYSTEM CHECKS
    SILENCED_SYSTEM_CHECKS = values.ListValue(SILENCED_SYSTEM_CHECKS)

    # SECURITY MIDDLEWARE
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(SECURE_BROWSER_XSS_FILTER)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(
        SECURE_CONTENT_TYPE_NOSNIFF)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(
        SECURE_HSTS_INCLUDE_SUBDOMAINS)
    SECURE_HSTS_PRELOAD = values.BooleanValue(SECURE_HSTS_PRELOAD)
    SECURE_HSTS_SECONDS = values.IntegerValue(SECURE_HSTS_SECONDS)
    SECURE_REDIRECT_EXEMPT = values.ListValue(SECURE_REDIRECT_EXEMPT)
    SECURE_REFERRER_POLICY = values.Value(SECURE_REFERRER_POLICY)
    SECURE_SSL_HOST = values.Value(SECURE_SSL_HOST)
    SECURE_SSL_REDIRECT = values.BooleanValue(SECURE_SSL_REDIRECT)

    @classmethod
    def pre_setup(cls):
        super(BaseConfiguration, cls).pre_setup()
        if cls.DEBUG:
            cls.ALLOWED_HOSTS = ['*']


"""
https://github.com/django/django/blob/master/django/conf/global_settings.py
"""
