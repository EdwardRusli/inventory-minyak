from django.urls import path
from . import views

urlpatterns = [
    path('', views.ambil, name='ambil'),
    path('addambil/', views.addambil, name='addambil'),
    path('addambil/addrecordambil/', views.addrecordambil, name='addrecordambil'),
    path('deleteambil/<int:id>', views.deleteambil, name='deleteambil'),
    path('updateambil/<int:id>', views.updateambil, name='updateambil'),
    path('updateambil/updaterecordambil/<int:id>', views.updaterecordambil, name='updaterecordambil'),
]