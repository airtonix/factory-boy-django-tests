#!/usr/bin/env python

__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

import logging

from django.test import TestCase
from django.db.models import get_model
from django.conf import settings

from . import foundry


logger = logging.getLogger('factory')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class ProductTypeTest(TestCase):

    # def setUp(self):



    def test_product_type(self):
        foundry.SluggedThingFactory.create_batch(45)
