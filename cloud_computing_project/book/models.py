from django.db import models

class Book(models.Model):
    name = models.CharField(null=False, max_length=512)
    author_name = models.CharField(null=False, max_length=512)
    year = models.DateField()
    price = models.IntegerField()