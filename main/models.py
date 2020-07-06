from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from audiofield.fields import AudioField
from tinymce.models import HTMLField
import os.path

# Create your models here.
class Site(models.Model):
    site_title = models.CharField(max_length=200)
    site_content = HTMLField()
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

class Resume(models.Model):
    resume_category = models.CharField(max_length=200)
    resume_data = HTMLField()

    def __str__(self):
        return self.resume_category
