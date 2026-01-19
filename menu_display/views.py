import os
import time
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from datetime import datetime

# Import Class 
from .logic.Barang import Barang as BarangClass
from .logic.Admin import Admin as AdminClass
from .logic.Assistant import Assistant as AssistantClass
from .logic.Transaksi import Transaksi as TransaksiClass
from .logic.Detail_Transaksi import Detail_Transaksi as DetailTransaksiClass

# Import Model DB & Algoritma
from .models import Barang as BarangModel
from .models import Pegawai as PegawaiModel
from .models import Transaksi as TransaksiModel
from .models import DetailTransaksi as DetailModel

from .logic.Algorithms import quicksort

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
    pembeli1 = AbstractClass.pembeli("Iyan", 200)
    context = {
        'pembeli': pembeli1,
        'pler': "Makado"
    }
    

    return render(request, 'menu_display/index.html', context)


def tampilkan_about(request):
    nama = request.session.get('username')
    password = request.session.get('password')
    
    if not nama:
        return redirect('login')
    
    return render(request, 'about/about.html')


def tampilkan_dashboard(request):
    nama = request.session.get('username')
    if not nama:
        return redirect('login')
    
    barangMentah = BarangModel.objects.all()
    daftarBarang = []
    total_aset_warung = 0
    jumlah_stok_rendah = 0

    for barang in barangMentah:
        barangOOP = BarangClass(
            barang.id,
            barang.nama,
            barang.stok,
            barang.hargabeli,
            barang.hargajual
        )
        total_aset_warung += (int(barang.stok) * int(barang.hargajual))
        if barang.stok < 10:
            jumlah_stok_rendah += 1
        daftarBarang.append(barangOOP)
     
    context = {
        'daftarBarang': daftarBarang,
        'total_aset': total_aset_warung,
        'stok_rendah_count': jumlah_stok_rendah,
        'username': nama,
        'hak': request.session.get('hak')
    }
    return render(request, 'menu_display/dashboard.html', context)

#================================LOGIKA LOGIN=====================================
def tampilkan_login(request):
    if request.session.get('username'):
        return redirect('dashboard')

    if request.method == 'POST':
        username_input = request.POST.get('nama')
        password_input = request.POST.get('password')

        pegawai_db = PegawaiModel.objects.filter(nama=username_input, password=password_input).first()
        
        if pegawai_db:
            role = pegawai_db.id_status.nama_status.lower() 
            if role == 'admin':
                user_obj = AdminClass(pegawai_db.nama, pegawai_db.password, pegawai_db.nomor_telepon)
            else:
                user_obj = AssistantClass(pegawai_db.nama, pegawai_db.password, pegawai_db.nomor_telepon)

            request.session['ID'] = pegawai_db.id_pegawai
            request.session['username'] = user_obj.getNama()
            request.session['hak'] = role
            request.session['nomorHp'] = user_obj.getNomorTelepon()
            request.session['foto'] = pegawai_db.foto_profil
            return redirect('dashboard')
            
    return render(request, 'menu_display/login.html')

#================================LOGIKA PROFILE===============================
def tampilkan_profile(request, ID):
    if not request.session.get('username'):
        return redirect('login')
    
    # PERBAIKAN: Gunakan PegawaiModel
    pegawai = PegawaiModel.objects.get(id_pegawai=ID)
    context = {'ID': ID, 'pegawai': pegawai}
    return render(request, 'menu_display/profile.html', context)

def tampilkan_logout(request):
    request.session.clear()
    return redirect('login')

def update_profile(request, ID):
    if request.method == 'POST':
        p_db = PegawaiModel.objects.get(id_pegawai=ID) # PERBAIKAN: PegawaiModel
        role = request.session.get('hak')

        if role == 'admin':
            user_obj = AdminClass(p_db.nama, p_db.password, p_db.nomor_telepon)
        else:
            user_obj = AssistantClass(p_db.nama, p_db.password, p_db.nomor_telepon)

        # Update via Setter Logic
        user_obj.setNama(request.POST.get('nama'))
        user_obj.setNomorTelepon(request.POST.get('nomorHp'))
        
        p_db.nama = user_obj.getNama()
        p_db.nomor_telepon = user_obj.getNomorTelepon()
        p_db.save()
        
        request.session['username'] = p_db.nama
        return redirect('profile', ID=ID)

def upload_foto_saja(request, ID):
    if request.method == 'POST' and request.FILES.get('foto_input'):
        try:
            foto = request.FILES.get('foto_input')
            
            # Cek folder media/pegawai secara otomatis
            target_dir = os.path.join(settings.MEDIA_ROOT, 'pegawai')
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            fs = FileSystemStorage()
            # Gunakan timestamp agar nama file unik jika user upload berkali-kali
            import time
            ext = os.path.splitext(foto.name)[1]
            filename = fs.save(f"pegawai/{ID}_{int(time.time())}{ext}", foto)
            file_url = fs.url(filename)

            # Update Database
            pegawai = PegawaiModel.objects.get(id_pegawai=ID)
            pegawai.foto_profil = file_url
            pegawai.save()

            request.session['foto'] = file_url
            return JsonResponse({'success': True, 'url': file_url})
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)



#==================================LOGIKA BARANG============================
def tampilkan_gudang(request):
    nama = request.session.get('username')
    if not nama:
        return redirect('login')
    
    # AMBIL DARI DATABASE (Gunakan BarangModel)
    query_db = BarangModel.objects.all()
    
    # PROSES INSTANSI KE OOP (Gunakan BarangClass)
    daftar_objek_oop = []
    for b in query_db:
        # Pindahkan data dari DB ke Class Manual
        objek = BarangClass(
            ID=b.id, 
            nama=b.nama, 
            stok=b.stok, 
            hargaBeli=b.hargabeli, 
            hargaJual=b.hargajual
        )
        daftar_objek_oop.append(objek)

    # Jalankan sorting pada list objek OOP
    barang_terurut = quicksort(daftar_objek_oop)

    # Hitung total (Demonstrasi OOP)
    for items in barang_terurut:
        items.total = int(items.stok) * int(items.hargaJual) # Gunakan atribut dari Class
    
    p = Paginator(barang_terurut, 5)
    nomor_halaman = request.GET.get('page')
    objek_halaman = p.get_page(nomor_halaman)
    
    context = {
        'barang': objek_halaman
    }
    
    return render(request, 'menu_display/gudang.html', context)

def hapus_barang(request, id_barang):
    # Ambil data dari DB
    b_db = BarangModel.objects.get(id=id_barang)
    # Instansiasi OOP (Pamer ke dosen: "Ini pak, saya pakai class manual saya")
    objek = BarangClass(b_db.id, b_db.nama, b_db.stok, b_db.hargabeli, b_db.hargajual)
    # Gunakan method hapusBarang() untuk ambil ID
    target_id = objek.hapusBarang()
    BarangModel.objects.filter(id=target_id).delete()
    return redirect('gudang')


def tambah_barang(request):
    if request.method == "POST":
        # Ambil data dari form (perhatikan string di dalam .get)
        id_input = request.POST.get('id')
        nama_input = request.POST.get('nama')
        stok_input = request.POST.get('stok')
        beli_input = request.POST.get('hargaBeli')
        jual_input = request.POST.get('hargaJual')

        # Simpan ke Database
        BarangModel.objects.create(
            id=id_input, # Sesuaikan dengan primary_key=True di modelmu
            nama=nama_input,
            stok=int(stok_input),
            hargabeli=float(beli_input),
            hargajual=float(jual_input)
        )
        return redirect('gudang')
    
    return redirect('tambah-barang') # Jika bukan POST balik ke form

def tambahStok(request):
    if request.method == "POST":
        id_barang = request.POST.get('id_barang')
        jumlah = int(request.POST.get('jumlah', 0))
        
        # Gunakan ID (huruf besar) sesuai model kamu
        b_db = BarangModel.objects.filter(id=id_barang).first()
        
        if b_db:
            objek = BarangClass(b_db.id, b_db.nama, b_db.stok, b_db.hargabeli, b_db.hargajual)
            objek.tambahStok(jumlah)
            
            b_db.stok = objek.infoStok()
            b_db.save()
            
    return redirect('gudang')

def kurangiStok(request):
    if request.method == "POST":
        id_barang = request.POST.get('id_barang')
        jumlah = int(request.POST.get('jumlah', 0))
        
        b_db = BarangModel.objects.get(id=id_barang)
        objek = BarangClass(b_db.id, b_db.nama, b_db.stok, b_db.hargabeli, b_db.hargajual)
        
        # PANGGIL METHOD CLASS KURANGI
        objek.kurangiStok(jumlah)
        
        b_db.stok = objek.infoStok()
        b_db.save()
    return redirect('gudang')

def tampilkan_form_barang(request):
    nama = request.session.get('username')
    
    if not nama:
        return redirect('login')
    
    return render(request, 'menu_display/tambah.html' )



#====================================LOGIKA TRANSAKSI===========================

def tampilkan_transaksi(request):
    nama = request.session.get('username')
    if not nama: return redirect('login')
    
    tahun_saiki = datetime.now().strftime("%Y")
    last_trx = TransaksiModel.objects.order_by('-id_transaksi').first()
    new_id_num = (last_trx.id_transaksi + 1) if last_trx else 1
    
    context = {
        'next_id': f"TRX-{tahun_saiki}{str(new_id_num).zfill(3)}",
        'daftar_barang': BarangModel.objects.all() # PERBAIKAN: BarangModel
    }
    return render(request, 'menu_display/transaksi.html', context)

def tambah_transaksi(request):
    if request.method == "POST":
        # 1. Inisialisasi Wrapper Transaksi
        wrapper_trx = TransaksiClass(namaPembeli=request.POST.get('nama_pembeli'))
        
        # Ambil data dari form yang dikirimkan dan bentuknya List
        barang_ids = request.POST.getlist('item_barang[]')
        qtys = request.POST.getlist('item_qty[]')

        # 2. Proses Barang satu per satu
        for b_id, qty in zip(barang_ids, qtys):
            if not b_id or not qty: 
                continue
            
            # Ambil data dari Database
            try:
                b_db = BarangModel.objects.get(id=b_id)
            except BarangModel.DoesNotExist:
                continue

            # Bungkus ke dalam BarangClass
            wrap_barang = BarangClass(
                ID=b_db.id, 
                nama=b_db.nama, 
                stok=b_db.stok, 
                hargaBeli=b_db.hargabeli, 
                hargaJual=b_db.hargajual
            )
            
            # Buat Detail Transaksi Wrapper
            wrap_detail = DetailTransaksiClass(barang_obj=wrap_barang, kuantitas=int(qty))
            wrapper_trx.Pesanan(wrap_detail)
            
            # Kurangi Stok di Logic & Update ke DB
            wrap_barang.kurangiStok(int(qty))
            b_db.stok = wrap_barang.infoStok()
            b_db.save()

        # 3. Simpan Header Transaksi ke Database
        new_trx_db = TransaksiModel.objects.create(
            nama_pembeli=wrapper_trx.namaPembeli,
            tanggal=datetime.now().date(),
            total_harga=wrapper_trx.getTotalBayar(),
            id_pegawai_id=request.session.get('ID')
        )

        # 4. Simpan Detail Transaksi ke Database (BAGIAN KRUSIAL)
        for d in wrapper_trx.detailPesanan:
            DetailModel.objects.create(
                id_transaksi=new_trx_db,
                id_barang_id=d.getBarang().ID,
                jumlah=d.getKuantitas(),
                # TAMBAHKAN HARGA SATUAN DI SINI BIAR GAK INTEGRITY ERROR
                harga_satuan=d.getBarang().hargaJual, 
                subtotal_harga=d.getSubTotal() 
            )

        return redirect('dashboard')
        
    return redirect('transaksi')


def tampilkan_detail_transaksi(request, id_transaksi):
    nama = request.session.get('username')
    
    if not nama:
        return redirect('login')
    
    transaksi_db = Transaksi.objects.get(id_transaksi=id_transaksi)
    

    
    context = {
        'transaksi': transaksi_db
    }
    
    return render(request, 'menu_display/laporan.html', context)

def hapus_detail_transaksi(request, id_transaksi):
    pass

#=============================================================================


#====================================LOGIKA LAPORAN===========================

def tampilkan_laporan(request):
    nama = request.session.get('username')
    
    if not nama:
        return redirect('login')
    
    return render(request, 'menu_display/laporan.html')


#=============================================================================




def tampilkan_settings(request):
    nama = request.session.get('username')
    
    if not nama:
        return redirect('login')
    
    return render(request, 'menu_display/settings.html')

def tampilkan_staff(request):
    nama = request.session.get('username')
    
    if not nama:
        return redirect('login')
    
    return render(request, 'menu_display/staff.html')

def tampilkan_manage(request):
    nama = request.session.get('username')
    
    if not nama:
        return redirect('login')
    
    return render(request, 'menu_display/manage.html' )




