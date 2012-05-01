from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from ckeditor.widgets import CKEditorWidget


# Override flatpage admin
class FlatPageAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': CKEditorWidget(attrs={'class':'ckeditor'})},}
    
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)