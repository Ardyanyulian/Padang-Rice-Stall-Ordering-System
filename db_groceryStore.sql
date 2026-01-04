-- Pembersihan tabel
DROP TABLE IF EXISTS Barang;
DROP TABLE IF EXISTS Gudang;
DROP TABLE IF EXISTS Pegawai;
DROP TABLE IF EXISTS RoleStatus;

-- 1. Tabel RoleStatus (Normalisasi)
CREATE TABLE RoleStatus (
    id_status INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_status TEXT NOT NULL
);

-- 2. Tabel Pegawai (Ditambahkan kolom email dan foto_profil)
CREATE TABLE Pegawai (
    id_pegawai INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    nomor_telepon INTEGER,
    password TEXT NOT NULL,
    foto_profil TEXT, -- Menyimpan path: 'uploads/pegawai/iyan.jpg'
    id_status INTEGER,
    FOREIGN KEY (id_status) REFERENCES RoleStatus(id_status)
);

-- 3. Tabel Gudang (Kategori Bahan Pokok)
CREATE TABLE Gudang (
    ID TEXT PRIMARY KEY, 
    kategori TEXT,
    deskripsi TEXT
);

-- 4. Tabel Barang (Ditambahkan kolom gambar_produk)
CREATE TABLE Barang (
    ID TEXT PRIMARY KEY, 
    nama TEXT NOT NULL,
    stok INTEGER,
    hargaBeli REAL,
    hargaJual REAL,
    gambar_produk TEXT, -- Menyimpan path: 'uploads/barang/sosis.png'
    id_gudang TEXT,
    FOREIGN KEY (id_gudang) REFERENCES Gudang(ID)
);

-- --- INSERT DATA REALISTIS ---

INSERT INTO RoleStatus (nama_status) VALUES ('Admin'), ('Assistant');

-- Update Insert Pegawai (Foto dikosongkan dulu atau pakai path default)
INSERT INTO Pegawai (nama, email, nomor_telepon, password, foto_profil, id_status) VALUES 
('Ibu Owner', 'owner.berkah@email.com', 081234567, 'pass_ibu_123', 'static/img/profiles/owner.jpg', 1),
('Iyan Assistant', 'iyan.dev@email.com', 087765432, 'pass_iyan_123', 'static/img/profiles/iyan.jpg', 2);

-- Gudang Bahan Pokok
INSERT INTO Gudang (ID, kategori, deskripsi) 
VALUES ('G-POKOK', 'Sembako & Frozen', 'Penyimpanan bahan pokok dan makanan beku');

-- Barang dengan path gambar (Asumsi gambar ada di folder static/img/products/)
INSERT INTO Barang (ID, nama, stok, hargaBeli, hargaJual, gambar_produk, id_gudang) VALUES 
('B001', 'Minyak Goreng Filma 2L', 24, 32000.0, 36000.0, 'static/img/products/filma.jpg', 'G-POKOK'),
('B002', 'Beras Ramos Setra Ramos 5kg', 10, 68000.0, 75000.0, 'static/img/products/beras.jpg', 'G-POKOK'),
('B003', 'Gula Pasir Gulaku 1kg', 50, 14500.0, 17000.0, 'static/img/products/gulaku.jpg', 'G-POKOK'), 
('B005', 'Sosis Kimbo Reddi Sapi', 40, 2000.0, 3000.0, 'static/img/products/sosis_kimbo.jpg', 'G-POKOK');