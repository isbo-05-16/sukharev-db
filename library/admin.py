from django.contrib import admin
from rangefilter.filter import DateTimeRangeFilter
from advanced_filters.admin import AdminAdvancedFiltersMixin
from .models import Book, User, Book2

@admin.register(Book)
class BookAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('code', 'author', 'title', 'year', 'num')
    advanced_filter_fields = list_display
    search_fields = ['title','author']

@admin.register(User)
class UserAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name', 'middle_name', 'address')
    search_fields = list_display
    advanced_filter_fields = list_display

@admin.register(Book2)
class Book2Admin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('book', 'user', 'given_date', 'exp_date', 'recv_date')
    search_fields = ('user__code', 'book__code')
    advanced_filter_fields = (*search_fields, 'given_date', 'exp_date', 'recv_date')
    list_filter = (('given_date', DateTimeRangeFilter),
                   ('exp_date', DateTimeRangeFilter),
                   ('recv_date', DateTimeRangeFilter),)
