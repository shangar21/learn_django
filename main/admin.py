from django.contrib import admin
from .models import Site
from .models import Podder
from .models import Resume
from .models import Blog
#from froala_editor.widgets import FroalaEditor
#from martor.widgets import AdminMartorWidget
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

class SiteAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Date", {"fields":["site_published"]}),
        ("Title", {"fields":["site_title"]}),
        ("content", {"fields":["site_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


class PodderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Date", {"fields":["podder_published"]}),
        ("Title", {"fields":["podder_title"]}),
        ("content", {"fields":["podder_description"]}),
        ("Audio", {"fields":["podder_audio"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class ResumeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title", {"fields":["resume_category"]}),
        ("content", {"fields":["resume_data"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title", {"fields":["blog_title"]}),
        ("Description", {"fields":["blog_description"]}),
        ("Post", {"fields":["blog_post"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Site, SiteAdmin)
admin.site.register(Podder, PodderAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Blog, BlogAdmin)