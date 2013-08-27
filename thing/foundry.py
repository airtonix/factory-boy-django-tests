import random
import logging
import factory

from . import models


class CategoryFactory(factory.Factory):
    FACTORY_FOR = models.Category

    name = factory.Sequence(lambda n: "Category #{}".format(n) )


class SluggedThingFactory(factory.Factory):
    FACTORY_FOR = models.SluggedThing

    category = factory.SubFactory(CategoryFactory)

    active = factory.Iterator([True, False])
    name = factory.Sequence(lambda n: "SluggedThing #{}".format(n) )
    slug = factory.Sequence(lambda n: "sluggedthing-{}".format(n) )
