from django.http import HttpResponse, JsonResponse
from .models import Task
from django.template import loader
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from browser.serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

def index(request):
    latest_task = Task.objects.order_by('name')[:100]
    template = loader.get_template('browser/index.html')
    context = {
        'latest_task': latest_task,
    }
    return HttpResponse(template.render(context, request))
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'browser/detail.html', {'task': task})

@csrf_exempt
def task_list(request):
    """
    List all code snippets, or create a new task.
    """
    if request.method == 'GET':
        snippets = Task.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, pk):
    """
    Show the task in more detail.
    """
    try:
        snippet = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

class task_detail_view(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('task_id')
    serializer_class = TaskSerializer