from django.shortcuts import render
from .logic import percobaan

# menu_display/views.py
def tampilkan_menu(request):

    DATA_MENU = [
        {"id": 1, "nama": "Nasi Ayam Pop", "harga": 22000, "tersedia": True},
        {"id": 2, "nama": "Gulai Kepala Ikan Kakap", "harga": 35000, "tersedia": True},
        {"id": 3, "nama": "Telur Dadar Sayur", "harga": 10000, "tersedia": True},
        {"id": 4, "nama": "Es Teh Manis", "harga": 6000, "tersedia": False}, 
    ]

    context = {
        'judul_halaman': "Daftar Menu Khas Padang",
        'daftar_item': DATA_MENU,
        'nama_warung': "Warung Makan Berkah",
    }
    
    # PERBAIKAN: Hapus 'templates/' dari path string.
    # Django tahu ia harus mencari di folder templates/
    return render(request, 'menu_display/menu.html', context)


def tampilkan_index(request):
    pembeli1 = percobaan.pembeli("Iyan", 200)
    context = {
        'pembeli': pembeli1,
        'pler': "Makado"
    }
    

    return render(request, 'menu_display/index.html', context)


def tampilkan_about(request):
    return render(request, 'about/about.html')


def tampilkan_dashboard(request):
    return render(request, 'menu_display/dashboard.html')

def tampilkan_login(request):
    return render(request, 'menu_display/login.html')

def tampilkan_transaksi(request):
    return render(request, 'menu_display/transaksi.html')

def tampilkan_profile(request):
    return render(request, 'menu_display/profile.html')

def tampilkan_gudang(request):
    return render(request, 'menu_display/gudang.html')

def tampilkan_settings(request):
    return render(request, 'menu_display/settings.html')

def tampilkan_staff(request):
    return render(request, 'menu_display/staff.html')

def tampilkan_laporan(request):
    return render(request, 'menu_display/laporan.html')

def tampilkan_manage(request):
    return render(request, 'menu_display/manage.html' )

def tampilkan_tambah(request):
    return render(request, 'menu_display/tambah.html' )