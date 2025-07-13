from django.urls import path
from . import views

urlpatterns = [
    path('', views.extracao_view, name='extracao_view'),
    path('limpar/', views.limpar_banco_view, name='limpar_banco_view'),
]