import setuptools

setuptools.setup(
    name='django-configurations-base',
    version='2020.10.23',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
