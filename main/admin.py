from django.contrib import admin
from .models import Site
from mdeditor.widgets import MDEditorWidget
from django.db import models
# Register your models here.

class SiteAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Date", {"fields":["site_published"]}),
        ("Title", {"fields":["site_title"]}),
        ("content", {"fields":["site_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget()}
    }

admin.site.register(Site, SiteAdmin)