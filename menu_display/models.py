# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Barang(models.Model):
    id = models.TextField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nama = models.TextField()
    stok = models.IntegerField(blank=True, null=True)
    hargabeli = models.FloatField(db_column='hargaBeli', blank=True, null=True)  # Field name made lowercase.
    hargajual = models.FloatField(db_column='hargaJual', blank=True, null=True)  # Field name made lowercase.
    gambar_produk = models.TextField(blank=True, null=True)
    id_gudang = models.ForeignKey('Gudang', models.DO_NOTHING, db_column='id_gudang', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Barang'


class Gudang(models.Model):
    id = models.TextField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kategori = models.TextField(blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Gudang'


class Pegawai(models.Model):
    id_pegawai = models.AutoField(primary_key=True)
    nama = models.TextField()
    email = models.TextField(unique=True)
    nomor_telepon = models.IntegerField(blank=True, null=True)
    password = models.TextField()
    foto_profil = models.TextField(blank=True, null=True)
    id_status = models.ForeignKey('Rolestatus', models.DO_NOTHING, db_column='id_status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pegawai'


class Rolestatus(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'RoleStatus'
