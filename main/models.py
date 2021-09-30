from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from audiofield.fields import AudioField
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from django.urls import reverse
#from tinymce.models import HTMLField

import os.path

# Create your models here.
class Site(models.Model):
    site_title = models.CharField(max_length=200)
    site_content = models.TextField()
    site_published = models.DateTimeField("Date Published", default=timezone.now())

    def __str__(self):
        return self.site_title

class Podder(models.Model):
    podder_title = models.CharField(max_length=200)
    podder_description = models.TextField()
    podder_published = models.DateTimeField("Date Published", default=timezone.now())
    podder_audio = models.FileField(upload_to="audio")

    def __str__(self):
        return self.podder_title

class Podcast(models.Model):
    podcast_title = models.CharField(max_length=200)
    podcast_description = models.TextField()
    podder_cover_art = models.FileField(upload_to="images")
    podcast_url = models.CharField(max_length=500)

    def __str__(self):
        return self.podcast_title

class Resume(models.Model):
    resume_category = models.CharField(max_length=200)
    resume_data = models.TextField()

    def __str__(self):
        return self.resume_category

class Blog(models.Model):
    blog_title = models.CharField(max_length=300)
    blog_description = models.TextField()
    blog_post = models.TextField()

    def __str__(self):
        return self.blog_title
