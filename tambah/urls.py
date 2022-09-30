from django.urls import path
from . import views

urlpatterns = [
    path('', views.tambah, name='tambah'),
    path('addtambah/', views.addtambah, name='addtambah'),
    path('addtambah/addrecordtambah/', views.addrecordtambah, name='addrecordtambah'),
]