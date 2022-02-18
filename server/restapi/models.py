from django.db import models
import datetime

class Blogger(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=500)
    time = models.DateTimeField('Date', auto_now=True)