from django.contrib import admin
from .models import Site
from .models import Podder
from froala_editor.widgets import FroalaEditor
from martor.widgets import AdminMartorWidget
from django.db import models
# Register your models here.

class SiteAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Date", {"fields":["site_published"]}),
        ("Title", {"fields":["site_title"]}),
        ("content", {"fields":["site_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': FroalaEditor()}
    }

class PodderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Date", {"fields":["podder_published"]}),
        ("Title", {"fields":["podder_title"]}),
        ("content", {"fields":["podder_description"]}),
        ("Audio", {"fields":["podder_audio"]})
    ]


admin.site.register(Site, SiteAdmin)
admin.site.register(Podder, PodderAdmin)