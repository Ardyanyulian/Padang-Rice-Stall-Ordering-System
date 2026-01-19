class Detail_Transaksi:
    def __init__(self, barang_obj, kuantitas):
        # Atribut sesuai Class Diagram (Private nganggo __)
        self.__barang = barang_obj  # Iki instansiasi seko Class Barang (OOP Wrapper)
        self.__kuantitas = int(kuantitas)
        self.__subTotal = self.hitungSubTotal()

    def hitungSubTotal(self):
        # Ngambil hargaJual seko wrapper Barang, terus dikali kuantitas
        return float(self.__barang.hargaJual * self.__kuantitas)

    def infoPesanan(self):
        # Method nggo nampilke ringkasan detail per item
        return {
            "nama": self.__barang.nama,
            "harga": self.__barang.hargaJual,
            "qty": self.__kuantitas,
            "subtotal": self.__subTotal
        }
    
    # Getter nggo keperluan simpen neng DB utawa nampilke neng view
    def getSubTotal(self):
        return self.__subTotal
    
    def getBarang(self):
        return self.__barang
    
    def getKuantitas(self):
        return self.__kuantitas