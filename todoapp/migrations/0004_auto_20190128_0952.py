# Generated by Django 2.1.5 on 2019-01-28 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20190128_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo_tile',
            new_name='todo_title',
        ),
    ]
