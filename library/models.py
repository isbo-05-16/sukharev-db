from django.db import models
from django.contrib import admin
from django.forms import ModelForm

class Book(models.Model):
    code = models.CharField(max_length=32, primary_key=True)
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    year = models.SmallIntegerField()
    num = models.SmallIntegerField()

class User(models.Model):
    code = models.CharField(max_length=32, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

class Book2(models.Model):
    book = models.ForeignKey(Book, to_field='code', on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field='code', on_delete=models.CASCADE)
    given_date = models.DateTimeField()
    exp_date = models.DateTimeField()
    recv_date = models.DateTimeField()
