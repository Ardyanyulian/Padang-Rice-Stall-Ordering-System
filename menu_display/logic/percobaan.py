class Manusia:
    def __init__(self, nama):
        self.nama = nama
    
    def cetakInfo(self):
        return f"Nama saya adalah {self.nama}"
    
class pembeli(Manusia):
    def __init__(self, nama, saldo):
        super().__init__(nama)
        self.saldo = saldo
    
    def cetakInfo(self):
        nama = super().cetakInfo()
        return f"{nama} <br> Saldo : {self.saldo}"

class kasir(Manusia):
    def __init__(self, nama):
        super().__init__(nama)
        self.pesanan = []



