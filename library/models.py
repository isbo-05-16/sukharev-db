from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from rangefilter.filter import DateTimeRangeFilter
from advanced_filters.admin import AdminAdvancedFiltersMixin

class Book(models.Model):
    code = models.CharField(max_length=32, primary_key=True)
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    year = models.SmallIntegerField()
    num = models.SmallIntegerField()

@admin.register(Book)
class BookAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('code', 'author', 'title', 'year', 'num')
#    list_filter = ('code', 'author', 'title', 'year', 'num')
    advanced_filter_fields = list_display
    search_fields = ['title','author']

class User(models.Model):
    code = models.CharField(max_length=32, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

@admin.register(User)
class UserAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name', 'middle_name', 'address')
    search_fields = list_display
    advanced_filter_fields = list_display

class Book2(models.Model):
    book = models.ForeignKey(Book, to_field='code', on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field='code', on_delete=models.CASCADE)
    given_date = models.DateTimeField()
    exp_date = models.DateTimeField()
    recv_date = models.DateTimeField()

@admin.register(Book2)
class Book2Admin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('book', 'user', 'given_date', 'exp_date', 'recv_date')
    search_fields = ('user__code', 'book__code')
    advanced_filter_fields = (*search_fields, 'given_date', 'exp_date', 'recv_date')
    list_filter = (('given_date', DateTimeRangeFilter),
                   ('exp_date', DateTimeRangeFilter),
                   ('recv_date', DateTimeRangeFilter),)
