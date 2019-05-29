from django.db import models

class Pet(models.Model):
  name = models.CharField(max_length=255)
  


class Breed(models.Model):
  name = models.CharField(max_length=255)
  customer = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name= 'pet')