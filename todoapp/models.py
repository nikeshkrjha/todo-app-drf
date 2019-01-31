from django.db import models
from django import forms
import datetime
from django.contrib.auth.models import User, Group
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    todo_title = models.CharField(max_length=200,blank=True,verbose_name='Title',)
    todo_desc = models.TextField(default='', blank=False, verbose_name='Description')
    created_date = models.DateField(verbose_name='Created Date', default=timezone.now())
    updated_date = models.DateField(verbose_name='Updated Date', default=timezone.now())
    todo_status = models.BooleanField(default=False,verbose_name='Completed',)
    created_by = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE,null=True, blank=True)
    category = models.ForeignKey('Category', related_name='note_category', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.todo_title

    @staticmethod
    def autocomplete_search_fields():
        return 'todo_title',

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     if self.pk is None:
    #         self.created_date = datetime.date.today()
    #     # self.created_by = UserSerializer(data=self.created_by).data
    #     self.updated_date = datetime.date.today()
    #     super(Todo, self).save()
    #     # super(Todo, self).save(*args, **kwargs)





class AppUser(User):
    user_email = models.EmailField(blank=False, verbose_name="Email", )
    user_name = models.CharField(blank=False, verbose_name="Username", max_length=100)


class Category(models.Model):
    category_name = models.CharField(max_length=200,blank=True,verbose_name='Category Name',)
    created_by = created_by = models.ForeignKey('auth.User', related_name='todo_catt', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.category_name


