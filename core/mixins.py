import datetime
from django.db import models

class DateCreatedTracking(models.Model):
    date_created = models.DateTimeField(editable=False, auto_now_add=True, default=datetime.datetime.now())

    class Meta:
        abstract = True

class DateTracking(DateCreatedTracking):
    last_updated = models.DateTimeField(editable=False, auto_now=True, default=datetime.datetime.now())

    class Meta:
        abstract = True