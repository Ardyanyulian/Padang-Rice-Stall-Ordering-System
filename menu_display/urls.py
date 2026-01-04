# menu_display/urls.py
from django.urls import path
from . import views 
from order_core import settings
from django.conf.urls.static import static
urlpatterns = [
    # Ketika alamat utama diakses (URL kosong), panggil views.tampilkan_menu
    path('', views.tampilkan_login, name='login'),
    path('daftar_menu/', views.tampilkan_menu, name='daftar_menu'),
    path('about/', views.tampilkan_about , name='about'),
    path('dashboard/', views.tampilkan_dashboard , name='dashboard'),
    path('login/', views.tampilkan_login , name='login'),
    path('transaksi/', views.tampilkan_transaksi , name='transaksi'),
    path('profile/<int:ID>/', views.tampilkan_profile , name='profile'),
    path('gudang/', views.tampilkan_gudang , name='gudang'),
    path('settings/', views.tampilkan_settings , name='settings'),
    path('staff/', views.tampilkan_staff , name='staff'),
    path('laporan/', views.tampilkan_laporan , name='laporan'),
    path('manage/', views.tampilkan_manage , name='manage'),
    path('tambah/', views.tampilkan_tambah , name='tambah'),
    path('logout/', views.tampilkan_logout , name='logout'),
    path('update/<int:ID>/', views.update, name='update_profil'),
    path('upload-foto/<int:ID>/', views.upload_foto_saja, name='upload_foto_saja'),
    path('gudang/tambah', views.tambah_barang, name='tambah_barang'),
    path('gudang/update-stok/', views.tambahStok, name='tambah_stok'),
    path('gudang/kurangi-stok/', views.kurangiStok, name='kurangi_stok'),
    path('gudang/hapus/<str:id_barang>/', views.hapus_barang, name='hapus_barang'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)