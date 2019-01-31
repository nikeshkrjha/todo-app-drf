from django.contrib import admin
from django import forms
from django.forms import TextInput, Textarea

# Register your models here.

from .models import Todo, AppUser, Category
from jet.admin import CompactInline


# class CategoryInline(admin.TabularInline):
#     model = Todo
#     extra = 1
#     show_change_link = True
#
#
# class StateCitiesInline(CompactInline):
#     model = Todo
#     extra = 1
#     show_change_link = True

class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo_title', 'todo_desc', 'created_date', 'updated_date', 'todo_status', 'created_by', 'category')
    exclude = ('created_by','updated_date')
    search_fields = ('todo_title', 'todo_desc', )
    list_filter = ('created_by','category')
    list_per_page = 15
    # inlines = (CategoryInline, )
    # form = TodoForm

    class Meta:
        model = Todo

    # associate user with specific todo entry
    def save_model(self, request, obj, form, change):
        print("Nikesh Jha")
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_by')
    exclude = ('created_by',)
    search_fields = ('category_name',)

    # form = TodoForm

    class Meta:
        model = Category

    # associate user with specific todo entry
    def save_model(self, request, obj, form, change):
        print("Nikesh Jha")
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Todo, TodoAdmin)
# admin.site.register(AppUser)
admin.site.register(Category, CategoryAdmin)

