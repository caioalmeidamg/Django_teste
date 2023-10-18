from django.urls import path
from .views import ProdutoListCreateView

#urls.py é o arquivo que detecta as rotas da aplicação

#Esse arquivo para rotas serve como uma  espécie de handler da aplicação
urlpatterns = [
    path('produtos/', ProdutoListCreateView.as_view(), name='produto-list-create'),
]