from django.db import models


class ActivatedModelBase(models.Model):

    active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CategorisedModelBase(models.Model):
    category = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        pass


class Thing(ActivatedModelBase, CategorisedModelBase):
    name = models.CharField(max_length=255)

    class Meta:
        pass


class SluggedThing(Thing):
    slug = models.SlugField(max_length=255)

    class Meta:
        pass


