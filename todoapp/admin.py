from django.contrib import admin
from django import forms
from django.forms import TextInput, Textarea

# Register your models here.

from .models import Todo, AppUser


class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo_title', 'todo_desc', 'created_date', 'updated_date', 'todo_status', 'created_by')
    # form = TodoForm

    class Meta:
        model = Todo


admin.site.register(Todo, TodoAdmin)
admin.site.register(AppUser)

