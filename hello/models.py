from django.db import models
import datetime

# Create your models here.
class Newsletter(models.Model):
    email_address = models.CharField(max_length=200)
    date_added = models.DateTimeField('date_added',default=datetime.datetime.now)