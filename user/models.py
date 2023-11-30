from django.db import models

class Autorune(models.Model):
    name = models.CharField()
    second_name = models.CharField()
    numbars = models.IntegerField(unique=True)
    adres = models.CharField()
    images = models.ImageField()
