from django.contrib import admin
from django import forms
from django.forms import TextInput, Textarea

# Register your models here.

from .models import Todo, AppUser


class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo_title', 'todo_desc', 'created_date', 'updated_date', 'todo_status', 'created_by')
    exclude = ('created_by',)
    search_fields = ('todo_title', 'todo_desc', )
    # form = TodoForm

    class Meta:
        model = Todo

    # associate user with specific todo entry
    def save_model(self, request, obj, form, change):
        print("Nikesh Jha")
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Todo, TodoAdmin)
admin.site.register(AppUser)

