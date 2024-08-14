import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Event(models.Model):
    CountryCodes = (
        ("PH", _("+63")),
        ("AU", _("+61")),
        ("NZ", _("+64"))
    )
    
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="static/images")
    email = models.EmailField()
    contact = models.CharField(max_length=25)
    dial_code = models.CharField(max_length=3, choices=CountryCodes, default=CountryCodes.PH)
    date_start = models.DateField("date start")
    date_end = models.DateField("date end")
    date_created = models.DateTimeField("date created", auto_now=True)
    date_updated = models.DateTimeField("date updated", auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @admin.display(
        boolean=True,
        ordering="date_start",
        description="Published recently?",
    )
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_created <= now