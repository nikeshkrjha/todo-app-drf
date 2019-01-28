from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todos_list),
    path('todos/<int:pk>/', views.todo_detail),
]