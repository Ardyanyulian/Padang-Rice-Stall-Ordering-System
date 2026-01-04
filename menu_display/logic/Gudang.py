
class Gudang:
    def __init__(self, ID, kategori, deskripsi):
        self.ID = ID
        self.kategori = kategori
        self.deskripsi = deskripsi
        self.daftarBarang = []

    def setKategori(self, _kategori):
        self.kategori = _kategori

    def setDeskripsi(self, _deskripsi):
        self.deskripsi = _deskripsi

    def getKategori(self):
        return self.kategori

    def getDeskripsi(self):
        return self.deskripsi

