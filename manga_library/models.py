from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField()

class Series(models.Model):
    name = models.TextField()

class Manga(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    series = models.ForeignKey(Series, on_delete = models.CASCADE)
    title = models.TextField()
    volume_number = models.IntegerField()

