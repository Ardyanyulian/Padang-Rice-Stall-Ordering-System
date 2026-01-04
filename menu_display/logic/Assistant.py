from menu_display.logic.AbstractClass import Manusia



class Assistant(Manusia):
    def __init__(self, nama, password, nomor_telepon):
        super().__init__(nama, nomor_telepon)
        self.password = password
    
    def kelolaBarangKhusus():
        return True
    
    def getNama(self):
        return self.nama

    def getPassword(self):
        return self.password

    def getNomorTelepon(self):
        return self.nomor_telepon

    def setNama(self, _nama):
        self.nama = _nama

    def setPassword(self, _password):
        self.password = _password       

    def setNomorTelepon(self, _nomor_telepon):
        self.nomor_telepon = _nomor_telepon



