# menu_display/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    # Ketika alamat utama diakses (URL kosong), panggil views.tampilkan_menu
    path('', views.tampilkan_index, name='index'),
    path('daftar_menu/', views.tampilkan_menu, name='daftar_menu'),
    path('about/', views.tampilkan_about , name='about')
]