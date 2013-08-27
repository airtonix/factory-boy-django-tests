#!/usr/bin/env python
from djeasytests.testsetup import TestSetup, default_settings

default_settings.update(dict(
    ROOT_URLCONF='thing.urls',
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'thing',
    ]
))

testsetup = TestSetup(appname='thing',
                      default_settings=default_settings)

if __name__ == '__main__':
    testsetup.run('tests')