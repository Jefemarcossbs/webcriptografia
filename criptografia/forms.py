from django import forms

class Gerar_Chave(forms.Form):
    nome_chave = forms.CharField(max_length=10,min_length=3,
                                 help_text='Entre com um nome para a chave minimo 3 maximo 10 caracteres', required=True)   