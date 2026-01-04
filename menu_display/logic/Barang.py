
class Barang:
    def __init__(self, ID, nama, stok, hargaBeli, hargaJual):
        self.ID = ID
        self.nama = nama
        self.stok = stok
        self.hargaBeli = hargaBeli
        self.hargaJual = hargaJual

    def hapusBarang(self):
        return self.ID

    def tambahStok(self, jumlahStok):
        self.stok += jumlahStok

    def infoStok(self):
        return self.stok
    
    def kurangiStok(self, jumlahStok):
        if self.stok > 0:
            self.stok -= jumlahStok
        else:
            return 0

    def getNama(self):
        return self.nama

    def setNama(self, _nama):
        self.nama = _nama

    def getHargaBeli(self):
        return self.hargaBeli   

    def setHargaBeli(self, _hargaBeli):
        self.hargaBeli = _hargaBeli

    def getHargaJual(self):
        return self.hargaJual

    def setHargaJual(self, _hargaJual):
        self.hargaJual = _hargaJual

    def getID(self):
        return self.ID