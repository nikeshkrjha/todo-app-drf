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
    created_by = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.todo_title + " " + str(self.created_date)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        # lexer = get_lexer_by_name(self.language)
        # linenos = 'table' if self.linenos else False
        # options = {'title': self.title} if self.title else {}
        # formatter = HtmlFormatter(style=self.style, linenos=linenos,
        #                           full=True, **options)
        # self.highlighted = highlight(self.code, lexer, formatter)
        if self.pk is None:
            self.created_date = datetime.date.today()
        self.updated_date = datetime.date.today()
        super(Todo, self).save()
        super(Todo, self).save(*args, **kwargs)




class AppUser(User):
    user_email = models.EmailField(blank=False, verbose_name="Email", )
    user_name = models.CharField(blank=False, verbose_name="Username", max_length=100)


