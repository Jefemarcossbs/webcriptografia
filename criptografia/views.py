from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template_index = loader.get_template('index.html')
    return HttpResponse(template_index.render())