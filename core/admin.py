from __future__ import division
from __future__ import absolute_import

from django.contrib import admin

from core.models import  Course, GraduationYear, BoardMember, ExecMember, ApplicantPoll, Applicant


class ApplicantPollAdmin(admin.ModelAdmin):
    fields = ['active']
admin.site.register(ApplicantPoll, ApplicantPollAdmin)

class ApplicantAdmin(admin.ModelAdmin):
    fields = ['applicantPoll', 'first_name', 'last_name', 'email', 'graduation_year', 'major', 'image']
admin.site.register(Applicant, ApplicantAdmin)


class BoardMemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(BoardMember, BoardMemberAdmin)


class ExecMemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExecMember, ExecMemberAdmin)


class GraduationYearAdmin(admin.ModelAdmin):
    fields = ['year']
    ordering = ('-year',)

admin.site.register(GraduationYear, GraduationYearAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'num', 'sort_order')
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)
