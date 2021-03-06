from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from todoapp.models import Category, Todo
from todoapp.permissions import IsOwnerOrReadOnly
from todoapp.serlializers import (CategorySerializer, TodoSerializer,
                                  UserSerializer)

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the todoapp index.")


class TodoList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

    def get(self, request, format=None):
        snippets = Todo.objects.all()
        serializer = TodoSerializer(snippets, many=True)
        categories = Category.objects.all()
        serializer2 = CategorySerializer(categories, many=True)

        return Response({'data': {'notes': serializer.data, 'categories': serializer2.data}})

    def post(self, request, format=None):
        print(request.data['todos'])
        serializer = TodoSerializer(data=request.data['todos'])
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
