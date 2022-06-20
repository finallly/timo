from datetime import datetime

from django.db import models
from django.core.validators import FileExtensionValidator


class Article(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    image = models.ImageField(upload_to='photos')
    link = models.CharField(max_length=512)
    date_uploaded = models.DateTimeField(default=datetime.now)


class Photo(models.Model):
    description = models.CharField(max_length=256)
    image = models.FileField(upload_to='photos')
    date_uploaded = models.DateTimeField(default=datetime.now)


class Video(models.Model):
    video = models.FileField(
        upload_to='videos',
        validators=[FileExtensionValidator(
            allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv']
        )]
    )
    description = models.CharField(max_length=256)
    date_uploaded = models.DateTimeField(default=datetime.now)
