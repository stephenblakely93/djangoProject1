from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=25, primary_key=True)
    properties = models.CharField(max_length=200, default='')
    parameters = models.CharField(max_length=200, default='')
    settings = models.CharField(max_length=200, default='')
    notes = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.customer_name
