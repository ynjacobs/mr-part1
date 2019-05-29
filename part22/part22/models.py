from django.db import models

class Worker(models.Model):
  name = models.CharField(max_length=255)
  wage = models.IntegerField()
  


class Shift(models.Model):
   day = models.CharField(max_length=255)
   shift = models.TextField(max_length=1000)
   workers = models.ManyToManyField(Worker, related_name='worker')