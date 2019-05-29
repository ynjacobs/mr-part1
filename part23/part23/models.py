from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255)
  author_name = models.CharField(max_length=255)


class Chapter(models.Model):
  title = models.CharField(max_length=255)
  number = models.IntegerField()
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name= 'chapters')


class Reader(models.Model):
  name = models.CharField(max_length=255)
  age = models.IntegerField()
  book = models.ManyToManyField(Book, related_name='reader')

class Author(models.Model):
  name = models.CharField(max_length=255)
  books = models.ManyToManyField(Book, related_name='author')
  

