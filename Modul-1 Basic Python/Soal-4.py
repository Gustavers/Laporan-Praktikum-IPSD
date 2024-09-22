import csv

def baca_csv_ke_list(nama_file):
    nilai_mahasiswa = []
    
    try:
        # Membaca file CSV
        with open(nama_file, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) == 1:  # Pastikan hanya ada satu kolom (nilai)
                    try:
                        nilai = float(row[0].strip())  # Konversi nilai ke float
                        nilai_mahasiswa.append(nilai)
                    except ValueError:
                        print(f"Nilai tidak valid pada baris: {row}")
                else:
                    print(f"Baris data tidak valid: {row}")
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return None

    return nilai_mahasiswa

def hitung_rata_rata(nilai_mahasiswa):
    rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa) if nilai_mahasiswa else 0
    return rata_rata

def tampilkan_mahasiswa_terbaik_terburuk(nilai_mahasiswa):
    if nilai_mahasiswa:
        nilai_tertinggi = max(nilai_mahasiswa)
        nilai_terendah = min(nilai_mahasiswa)
        mahasiswa_terbaik = nilai_mahasiswa.index(nilai_tertinggi) + 1  # Indeks ke nomor mahasiswa
        mahasiswa_terburuk = nilai_mahasiswa.index(nilai_terendah) + 1
    
        print(f"Mahasiswa dengan nilai tertinggi: Mahasiswa {mahasiswa_terbaik} dengan nilai {nilai_tertinggi:.2f}")
        print(f"Mahasiswa dengan nilai terendah: Mahasiswa {mahasiswa_terburuk} dengan nilai {nilai_terendah:.2f}")
    else:
        print("Tidak ada data mahasiswa yang valid.")

# Main program
nama_file = 'nilai.csv'  # File CSV yang hanya berisi nilai

# Langkah 1: Membaca file CSV dan menyimpan datanya ke dalam list
nilai_mahasiswa = baca_csv_ke_list(nama_file)

if nilai_mahasiswa:
    # Langkah 2: Menghitung rata-rata nilai mahasiswa
    rata_rata = hitung_rata_rata(nilai_mahasiswa)
    print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")

    # Langkah 3: Menampilkan mahasiswa dengan nilai tertinggi dan terendah
    tampilkan_mahasiswa_terbaik_terburuk(nilai_mahasiswa)
