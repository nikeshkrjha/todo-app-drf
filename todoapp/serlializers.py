from rest_framework import serializers
from .models import Todo, AppUser


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'todo_title', 'todo_desc', 'created_date', 'updated_date', 'todo_status', 'created_by')