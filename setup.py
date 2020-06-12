from setuptools import setup

setup(
    name='django-configurations-base',
    version='2020.6.11',
    install_requires=[
        'dj-database-url',
        'django-configurations',
        'django-configurations-apps',
        'django-configurations-templates',
        'setuptools',
    ],
    packages=[
        'django_configurations_base',
    ],
)
