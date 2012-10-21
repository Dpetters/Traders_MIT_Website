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
    major = models.ManyToManyField(Course, related_name = "first_major", null=True)
    website = models.URLField(verify_exists=False, blank = True, null=True)
    image = models.ImageField(upload_to=get_image_filename, blank=True, null=True)
    co_president = models.BooleanField(default=False)
    blurb = models.TextField(blank=True, null=True)
    
    joined = models.DateTimeField(default=datetime.datetime.now())
    left = models.DateTimeField(blank=True, null=True)
    
    objects = BoardMemberManager()

class ApplicantPoll(models.Model):
    date = models.DateField(auto_now_add=True)
    
    active = models.BooleanField(default=True) 
    
    completed_by = models.ManyToManyField(ExecMember)
 
    def __unicode__(self):
        return self.date.strftime("%Y %B")


class Applicant(models.Model):
    applicantPoll = models.ForeignKey(ApplicantPoll)

    

    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('E-mail Address')   
    graduation_year = models.ForeignKey(GraduationYear, null=True)
    major = models.ManyToManyField(Course, blank=True, null=True) 
    website = models.URLField(verify_exists=False, blank = True, null=True)
    image = models.ImageField(upload_to=get_image_filename, blank=True, null=True)

    positives = models.TextField(null=True)
    negatives = models.TextField(null=True)
   
    score = models.IntegerField(default=0)
   

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
