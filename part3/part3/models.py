from django.db import models

class Actor(models.Model):
  name = models.CharField(max_length=255)
  


class Role(models.Model):
  title = models.CharField(max_length=255)
  customer = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name= 'actor')

