from django.db import models


class StandardModel(models.Model):
    field_one = models.CharField(max_length=255)
    field_two = models.CharField(max_length=255)
    field_three = models.CharField(max_length=255)


class StandardModelTwo(models.Model):
    parent_model = models.ForeignKey('StandardModel')
    field_one = models.CharField(max_length=255)
    field_two = models.CharField(max_length=255)
    field_three = models.CharField(max_length=255)
