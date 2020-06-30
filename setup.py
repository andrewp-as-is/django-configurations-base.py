import setuptools

setuptools.setup(
    name='django-configurations-base',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
