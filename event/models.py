from datetime import datetime

from django.db import models

from core import mixins as core_mixins


class Event(core_mixins.DateCreatedTracking):
    name = models.CharField(max_length=85)
    end_datetime = models.DateTimeField(null=True, blank=True)
    
    attending_employers = models.TextField(null=True, blank=True)

    start_datetime = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()

    rsvp_url = models.URLField(blank=True, null=True)
    
    slideshow = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def is_past(self):
        if self.end_datetime:
            return self.end_datetime < datetime.now()
        return False
