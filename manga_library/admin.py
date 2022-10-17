from django.contrib import admin

# Register your models here.
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        ("name", {"fields": ["name"]})
    ]

class SeriesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("name", {"fields": ["name"]})
    ]

class MangaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("title", {"fields": ["title"]}),
        ("author", {"fields": ["author"]}),
        ("series", {"fields": ["series"]})
    ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Manga, MangaAdmin)

