from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import Gerar_Chave
import models
# Create your views here.
def index(request):
    form = Gerar_Chave()
    return render(request, 'index.html', {'form_generate_key': form})
   
def gerar_chave(request):
    form = Gerar_Chave(request.POST)
    if form.is_valid:
        chaveform = form['nome_chave'].value()
        chave = models.generate_keys(chaveform)
        print(form['nome_chave'].value())
    return HttpResponse(chave)
    