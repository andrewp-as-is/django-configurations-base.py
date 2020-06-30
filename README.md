<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-configurations-base.svg?maxAge=3600)](https://pypi.org/project/django-configurations-base/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-configurations-base.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-configurations-base.py/actions)

### Installation
```bash
$ [sudo] pip install django-configurations-base
```

#### Features
key | default value | env
-|-|-
`ALLOWED_HOSTS` | `['*']` (if `DEBUG=True`) | `DJANGO_ALLOWED_HOSTS`
`AUTHENTICATION_BACKENDS` | `['django.contrib.auth.backends.ModelBackend']` | `DJANGO_AUTHENTICATION_BACKENDS`
`AUTH_USER_MODEL` | `auth.User` | `DJANGO_AUTH_USER_MODEL`
`DATABASES` | `[]` |  `DJANGO_DATABASE_URL`, [dj-database-url](https://github.com/jacobian/dj-database-url)
`DEBUG` | | `DJANGO_DEBUG` `('yes', 'y', 'true', '1')`
`INSTALLED_APPS` | [django-configurations-apps](https://pypi.org/project/django-configurations-apps/) | `DJANGO_INSTALLED_APPS`, `DJANGO_APPS_FILE`, `DJANGO_APPS_FIND`, [django-configurations-apps](https://pypi.org/project/django-configurations-apps/)
`INTERNAL_IPS` | `[]`  | `DJANGO_INTERNAL_IPS`
`LANGUAGE_CODE` | `en-us`  | `DJANGO_LANGUAGE_CODE`
`LOGIN_REDIRECT_URL` | `/`  | `DJANGO_LOGIN_REDIRECT_URL`
`LOGOUT_REDIRECT_URL` | `/`  | `DJANGO_LOGOUT_REDIRECT_URL`
`MEDIA_URL` | `/media/`  | `DJANGO_MEDIA_URL`
`MEDIA_ROOT` | `os.path.join(BASE_DIR, 'media')` | `DJANGO_MEDIA_ROOT`
`MIDDLEWARE` | `MIDDLEWARE_FILE` | `DJANGO_MIDDLEWARE_FILE`
`ROOT_URLCONF` | `urls` | `DJANGO_ROOT_URLCONF`
`SECRET_KEY` | | `DJANGO_SECRET_KEY`
`SITE_ID` | | `DJANGO_SITE_ID`
`STATIC_URL` | `/static/` | `DJANGO_STATIC_URL`
`STATIC_ROOT` | `os.path.join(BASE_DIR, 'static')` | `DJANGO_STATIC_ROOT`
`STATICFILES_DIRS` | `os.path.join(BASE_DIR, 'assets')` (if `./assets/` exists) | `DJANGO_STATICFILES_DIRS`
`TEMPLATES` | [django-configurations-templates](https://pypi.org/project/django-configurations-templates/) | [django-configurations-templates](https://pypi.org/project/django-configurations-templates/)
`TIME_ZONE` | `UTC` | `DJANGO_TIME_ZONE`
`WSGI_APPLICATION` | `wsgi.application` | `DJANGO_WSGI_APPLICATION`


`INSTALLED_APPS` ([django-configurations-apps](https://pypi.org/project/django-configurations-apps/))

key  | default value | env
-|-|-
`INSTALLED_APPS` | `[]` | `DJANGO_INSTALLED_APPS`
`INSTALLED_APPS_FILE` | `None` | `DJANGO_INSTALLED_APPS_FILE`
`INSTALLED_APPS_FIND` | `True` | `DJANGO_INSTALLED_APPS_FIND` ('yes', 'y', 'true', '1')

`TEMPLATES` ([django-configurations-templates](https://pypi.org/project/django-configurations-templates/))

key  | default value | env
-|-|-
`TEMPLATES_BACKEND` | `django.template.backends.django.DjangoTemplates` | `DJANGO_TEMPLATES_BACKEND`
`TEMPLATES_DIRS` | `os.path.join(BASE_DIR,'templates')` | `DJANGO_TEMPLATES_DIRS`
`TEMPLATES_APP_DIRS` | `True` |`DJANGO_TEMPLATES_APP_DIRS` ('yes', 'y', 'true', '1')
`TEMPLATES_OPTIONS` | |
`TEMPLATES_CONTEXT_PROCESSORS` | `[]` | `DJANGO_TEMPLATES_CONTEXT_PROCESSORS`
`TEMPLATES_CONTEXT_PROCESSORS_FILE` | `None` | `DJANGO_TEMPLATES_CONTEXT_PROCESSORS_FILE`
`TEMPLATES_LOADERS` | `[]` |

##### `settings.py`
```python
from django_configurations_base import BaseConfiguration

class Base(BaseConfiguration,...):
    APPS_FILE = 'apps.txt'
    APPS_FIND = True
    MIDDLEWARE_FILE = 'middleware.txt'
    TEMPLATES_CONTEXT_PROCESSORS_FILE = 'context_processors.txt'
```

#### Links
+   [django-configurations](https://github.com/jazzband/django-configurations)
+   [django-configurations-apps](https://pypi.org/project/django-configurations-apps/)
+   [django-configurations-templates](https://pypi.org/project/django-configurations-templates/)
+   [dj-database-url](https://github.com/jacobian/dj-database-url)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>