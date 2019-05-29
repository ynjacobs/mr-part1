from django.db import models

class Viewer(models.Model):
  name = models.CharField(max_length=255)
  age = models.IntegerField()
  


class Film(models.Model):
   title = models.CharField(max_length=255)
   year = models.TextField(max_length=1000)
   viewers = models.ManyToManyField(Viewer, related_name='films')