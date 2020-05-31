from django.db import models
from django.utils import timezone

# Create your models here.
class Site(models.Model):
    site_title = models.CharField(max_length=200)
    site_content = models.TextField()
    site_published = models.DateTimeField("Date Published", default=timezone.now())

    def __str__(self):
        return self.site_title