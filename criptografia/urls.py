from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('newkey/', views.gerar_chave, name='gerar_chave'),
]