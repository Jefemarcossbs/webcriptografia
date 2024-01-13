from django.shortcuts import render
from django.http import HttpResponse
from .forms import Gerar_Chave
from .models import new_key
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
        #fl_path = ‘/file/path'
        #filename = ‘downloaded_file_name.extension’
        #fl = open(fl_path, 'r’)
        #mime_type, _ = mimetypes.guess_type(fl_path)
        #response = HttpResponse(fl, content_type=mime_type)
        #response['Content-Disposition'] = "attachment; filename=%s" % filename
        #return response

        print(generate_new_key)
    return HttpResponse(chaveform)
    