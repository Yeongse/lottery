from django.urls import path

from . import views

app_name = 'extract'

urlpatterns = [
    path('', views.index, name='index'), 
    path('loto6', views.loto6, name='loto6')
]