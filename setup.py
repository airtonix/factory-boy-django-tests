from setuptools import setup
from setuptools import find_packages
import os

setup(
    name='isolated-factory-boy-django-test',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'Django==1.5.2',
        'django-easytests==0.9',
        'factory-boy==2.1.2',
    ],
    author='Zenobius Jiricek',
    author_email='airtonix@gmail.com',
    description='simple test demonstrating some problems with factory boy and django abstract models',
    license='MIT',
    keywords='django, factory-boy',
    include_package_data=True,
)

