from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Student

@register(Student)
class StudentAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'course', 'year_level')
