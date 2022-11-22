from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField()

class User(models.Model):
    admin = models.BooleanField(default=False)
    token = models.CharField(max_length=50)
