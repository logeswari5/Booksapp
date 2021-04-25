from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField('ISBN', max_length = 25, unique = True)
    num_of_pages = models.IntegerField()
    image = models.ImageField(upload_to="#",null=True,blank=True)
    description = models.TextField(max_length = 3000)
    genre = models.ManyToManyField('Genre')
    publisher = models.ManyToManyField('Publisher')
    published_date = models.DateField(null = True, blank = True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=150, null=True)
    address = models.TextField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name