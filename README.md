# Factory Boy Django Abstract Model Test

This is to illustrate some problems I'm having with factory-boy and django.

Specifically, it is common in Django to create models from other abstract models (as demonstrated in `thing.models`)


## Install

```
mkdir ~/Dev/
cd ~/Dev/
git clone https://github.com/airtonix/factory-boy-django-tests/
cd factory-boy-django-tests
mkvirtualenv `basename $PWD`
pip install -r ./requirements.txt
python ./runtests.py
```
