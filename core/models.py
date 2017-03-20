from django.db import models
import json


class Brand(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Car(models.Model):
    brand = models.ForeignKey(Brand)
    name = models.CharField(max_length=100)

    def __str__(self):
        return json.dumps({'name': self.name, 'brand': self.brand.company_name})


class Fleet(models.Model):
    car_model = models.ForeignKey(Car)
    description = models.CharField(max_length=100)


