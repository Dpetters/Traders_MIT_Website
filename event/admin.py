from __future__ import division
from __future__ import absolute_import

from ckeditor.widgets import CKEditorWidget

from django import forms
from django.contrib import admin

from event.models import Event


class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        widgets = {
                   'description': CKEditorWidget(),
                   }

class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
admin.site.register(Event, EventAdmin)