from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    image = models.ImageField()
