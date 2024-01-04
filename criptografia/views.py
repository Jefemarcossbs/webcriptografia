from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import Gerar_Chave

# Create your views here.
def index(request):
    form = Gerar_Chave()
    print(request)
    return render(request, 'index.html', {'form_generate_key': form})


