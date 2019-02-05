from rest_framework import serializers
from todoapp.models import Todo, AppUser, Category
from django.contrib.auth.models import User



class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'todo_title', 'todo_desc', 'created_date', 'updated_date', 'todo_status', 'created_by', 'category')



class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ('id', 'username', 'todos', 'owner')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'created_by')
