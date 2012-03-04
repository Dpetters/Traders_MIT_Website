from __future__ import division
from __future__ import absolute_import

from django.contrib import admin

from core.models import  Course, SchoolYear, GraduationYear, BoardMember, ExecMember


class BoardMemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(BoardMember, BoardMemberAdmin)


class ExecMemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExecMember, ExecMemberAdmin)


class SchoolYearAdmin(admin.ModelAdmin):
    fields = ['name', 'name_plural']

admin.site.register(SchoolYear, SchoolYearAdmin)


class GraduationYearAdmin(admin.ModelAdmin):
    fields = ['year']
    ordering = ('-year',)

admin.site.register(GraduationYear, GraduationYearAdmin)


class CourseAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', 'num', 'sort_order')
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)