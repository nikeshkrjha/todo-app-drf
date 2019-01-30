from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todoapp/api/todos/', views.TodoList.as_view()),
    path('todoapp/api/todos/<int:pk>/', views.TodoDetail.as_view()),
    path('todoapp/api/users/', views.UserList.as_view()),
    path('todoapp/api/users/<int:pk>/', views.UserDetail.as_view()),
]