from django.db import models
from django import forms
import datetime
from django.contrib.auth.models import User, Group

# Create your models here.


class Todo(models.Model):
    todo_title = models.CharField(max_length=200,blank=True,verbose_name='Title',)
    todo_desc = models.TextField(default='', blank=False, verbose_name='Description')
    created_date = models.DateField(verbose_name='Created Date', default=datetime.date.today())
    updated_date = models.DateField(verbose_name='Updated Date', default=datetime.date.today())
    todo_status = models.BooleanField(default=False,verbose_name='Completed',)
    created_by = models.ForeignKey('AppUser', on_delete=models.CASCADE, )

    def __str__(self):
        return self.todo_title + " " + str(self.created_date)


class AppUser(User):
    user_email = models.EmailField(blank=False, verbose_name="Email", )
    user_name = models.CharField(blank=False, verbose_name="Username", max_length=100)


