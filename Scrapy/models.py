from django.db import models

# Create your models here.


class data(models.Model):
    x = models.CharField(max_length=200)