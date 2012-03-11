import datetime

from core.managers import BoardMemberManager
from core.model_helpers import get_image_filename

from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField
from django.db import models

class GraduationYear(models.Model):
    year = models.PositiveSmallIntegerField("Graduation Year", unique=True)

    class Meta:
        verbose_name = "Graduation Year"
        verbose_name_plural = "Graduation Years"

    def __unicode__(self):
        return str(self.year)


class Course(models.Model):
    name = models.CharField("Course Name", max_length=42, unique=True, help_text="Maximum 42 characters.")
    num = models.CharField("Course Number", max_length=10, help_text="Maximum 10 characters.")
    sort_order = models.FloatField(help_text='Topics will be ordered by the sort order. (Smallest at top.)')
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.num)
    
    class Meta:
        ordering = ['sort_order']


class BoardMember(models.Model):
    user = models.OneToOneField(User, unique=True)
    
    objects = BoardMemberManager()
    
    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
    
    class Meta:
        ordering = ['user__first_name']
        
class ExecMember(BoardMember):
    graduation_year = models.ForeignKey(GraduationYear, null=True)
    major = models.ForeignKey(Course, related_name = "first_major", null=True)
    website = models.URLField(verify_exists=False, blank = True, null=True)
    image = models.ImageField(upload_to=get_image_filename, blank=True, null=True)
    phone = PhoneNumberField("Main Contact Phone #", blank = True, null=True)
    blurb = models.TextField(blank=True, null=True)
    
    joined = models.DateTimeField(default=datetime.datetime.now())
    left = models.DateTimeField(blank=True, null=True)
    
    objects = BoardMemberManager()
