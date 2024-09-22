class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_info(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}"

    def hitung_usia(self, tahun_sekarang):
        return tahun_sekarang - self.tahun_terbit

# Membuat objek dari class Buku
buku1 = Buku("Belajar Python", "Budi Santoso", 2020)
buku2 = Buku("Data Science untuk Pemula", "Ani Lestari", 2019)
buku3 = Buku("Kecerdasan Buatan", "Siti Rahma", 2021)

# Tahun saat ini
tahun_sekarang = 2024

# Menampilkan informasi dan usia masing-masing buku
for buku in [buku1, buku2, buku3]:
    info = buku.tampilkan_info()
    usia = buku.hitung_usia(tahun_sekarang)
    print(info)
    print(f"Usia Buku: {usia} tahun\n")
