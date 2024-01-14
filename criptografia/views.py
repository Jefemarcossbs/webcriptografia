import mimetypes
from django.shortcuts import render
from django.http import HttpResponse 
from .forms import Gerar_Chave
from .models import new_key
import os
from django.conf import settings
from django.http import Http404
# Create your views here.
def index(request):
    form = Gerar_Chave()
    return render(request, 'index.html', {'form_generate_key': form})

#View que recebe o nome da chave e gera uma nova   
def gerar_chave(request):
    form = Gerar_Chave(request.POST)
    #valida o formulario recebido
    if form.is_valid:
        chaveform = form['nome_chave'].value()
        #chama função para gerar a chave
        generate_new_key = new_key.generate_keys(chaveform)

        fl_path = os.path.join(settings.MEDIA_ROOT, '{}{}'.format(chaveform,'.key'))
        with open(fl_path, 'rb') as fl_download:
            mime_type, _ = mimetypes.guess_type(fl_path)
            response = HttpResponse(fl_download.read(), content_type=mime_type)
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(fl_path)
            return response
    else:
        return HttpResponse(Http404)
