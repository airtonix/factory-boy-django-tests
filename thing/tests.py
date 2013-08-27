#!/usr/bin/env python

import logging

from django.test import TestCase
from django.db.models import get_model
from django.conf import settings

from . import foundry


logger = logging.getLogger('factory')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

db_logger = logging.getLogger('django.db.backends')
db_logger.setLevel(logging.DEBUG)
db_logger.addHandler(logging.StreamHandler())



class ProductTypeTest(TestCase):

    def test_product_type(self):
        foundry.SluggedThingFactory.create_batch(45)
