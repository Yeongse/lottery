from django.urls import path

from . import views

app_name = 'extract'

urlpatterns = [
    path('', views.index, name='index'), 
    path('loto6', views.loto6, name='loto6'), 
    path('loto7', views.loto7, name='loto7'), 
    path('miniloto', views.miniloto, name='miniloto'), 
]