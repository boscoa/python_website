

from django.shortcuts import render
from django.views import generic

from .models import Task

def IndexView(request):
    template_name = 'backlog/index.html'

    return render(request, template_name, context={'tasks': Task})

