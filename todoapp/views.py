from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from todoapp.models import Todo
from todoapp.serlializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the todoapp index.")


@api_view(['GET', 'POST'])
def todos_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    renderer_classes = (JSONRenderer,)
    if request.method == 'GET':
        snippets = Todo.objects.all()
        serializer = TodoSerializer(snippets, many=True)
        data = {'message': 'SUCCESS', 'data': serializer.data}
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
