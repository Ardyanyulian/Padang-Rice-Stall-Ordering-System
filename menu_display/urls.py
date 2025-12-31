# menu_display/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    # Ketika alamat utama diakses (URL kosong), panggil views.tampilkan_menu
    path('', views.tampilkan_login, name='login'),
    path('daftar_menu/', views.tampilkan_menu, name='daftar_menu'),
    path('about/', views.tampilkan_about , name='about'),
    path('dashboard/', views.tampilkan_dashboard , name='dashboard'),
    path('login/', views.tampilkan_login , name='login'),
    path('transaksi/', views.tampilkan_transaksi , name='transaksi'),
    path('profile/', views.tampilkan_profile , name='profile'),
    path('gudang/', views.tampilkan_gudang , name='gudang'),
    path('settings/', views.tampilkan_settings , name='settings'),
    path('staff/', views.tampilkan_staff , name='staff'),
    path('laporan/', views.tampilkan_laporan , name='laporan'),
    path('manage/', views.tampilkan_manage , name='manage'),
    path('tambah/', views.tampilkan_tambah , name='tambah'),
]