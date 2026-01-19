from datetime import date

class Transaksi:
    def __init__(self, namaPembeli):
        # Public & Private Atribut sesuai Diagram
        self.detailPesanan = [] # Array of Detail_Transaksi objects
        self.namaPembeli = namaPembeli
        self.__tanggalPesan = date.today()
        self.__totalBayar = 0.0

    def Pesanan(self, detail_obj):
        # Method nggo nambahke objek Detail_Transaksi neng array
        self.detailPesanan.append(detail_obj)
        # Update total bayar otomatis saben nambah pesanan
        self.hitungTotal()

    def hitungTotal(self):
        # Ngitung kabeh subtotal sing ono neng array detailPesanan
        self.__totalBayar = sum(detail.getSubTotal() for detail in self.detailPesanan)
        return self.__totalBayar

    def infoDetailPesanan(self):
        # Method nggo nampilke kabeh rincian transaksi (biasane nggo Nota)
        return [detail.infoPesanan() for detail in self.detailPesanan]

    # Getter & Helper
    def getTotalBayar(self):
        return self.__totalBayar
    
    def getTanggal(self):
        return self.__tanggalPesan