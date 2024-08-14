from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    image = models.TextField()
    email = models.EmailField()
    contact = models.CharField(max_length=25)
    dial_code = models.CharField(max_length=3)
    date_created = models.DateTimeField("date created")
    date_updated = models.DateTimeField("date updated")
    date_start = models.DateField("date start")
    date_end = models.DateField("date end")