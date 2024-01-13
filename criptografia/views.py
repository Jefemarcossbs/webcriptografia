import mimetypes
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Gerar_Chave
from .models import new_key
import os
from django.conf import settings
# Create your views here.
def index(request):
    form = Gerar_Chave()
    return render(request, 'index.html', {'form_generate_key': form})
   
def gerar_chave(request):
    form = Gerar_Chave(request.POST)
    if form.is_valid:
        chaveform = form['nome_chave'].value()
        generate_new_key = new_key.generate_keys(chaveform)
        
        ##retornar o dowload da chave
        #fl_path = '{}{}'.format(chaveform,'.key')
        fl_path = os.path.join(settings.MEDIA_ROOT, '{}{}'.format(chaveform,'.key'))
        with open(fl_path, 'rb') as fl_download:
            mime_type, _ = mimetypes.guess_type(fl_path)
            response = HttpResponse(fl_download.read(), content_type=mime_type)
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(fl_path)
            return response
        #mime_type, _ = mimetypes.guess_type(fl_path)
        
        #-filename = ‘downloaded_file_name.extension’
        #-fl = open(fl_path, 'r’)
        #-mime_type, _ = mimetypes.guess_type(fl_path)
        #-response = HttpResponse(fl, content_type=mime_type)
        #response['Content-Disposition'] = "attachment; filename=%s" % filename
        #return response
    