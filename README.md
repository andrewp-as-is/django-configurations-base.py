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

##### `settings.py`
```python
from django_configurations_base import BaseConfiguration

class Base(BaseConfiguration):
    ...
```

##### `.env`
```bash
DJANGO_STATIC=/static/
...
```

#### Links
+   [django-configurations](https://github.com/jazzband/django-configurations)
+   [django-configurations-apps](https://pypi.org/project/django-configurations-apps/)
+   [django-configurations-templates](https://pypi.org/project/django-configurations-templates/)
+   [dj-database-url](https://github.com/jacobian/dj-database-url)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
