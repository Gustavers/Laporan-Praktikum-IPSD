import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    percobaan_terbatas = 5  # Batasi percobaan menjadi 5 kali
    
    print("Selamat datang di permainan tebak angka!")
    print("Komputer telah memilih angka secara acak antara 1 hingga 100.")
    print(f"Kamu memiliki {percobaan_terbatas} kali kesempatan untuk menebak.")

    for percobaan in range(1, percobaan_terbatas + 1):
        try:
            # Input dari pengguna
            tebakan = int(input(f"Percobaan {percobaan}: Masukkan angka tebakanmu: "))
            
            # Cek apakah tebakan benar
            if tebakan == angka_rahasia:
                print(f"Selamat! Kamu berhasil menebak angka yang benar dalam {percobaan} percobaan!")
                break
            # Beri petunjuk kepada pemain
            elif tebakan < angka_rahasia:
                print("Angka tebakanmu terlalu kecil.")
            else:
                print("Angka tebakanmu terlalu besar.")
        except ValueError:
            # Jika input bukan angka
            print("Input tidak valid. Masukkan angka yang benar.")

    else:
        # Jika pemain kehabisan kesempatan
        print(f"Maaf, kamu kehabisan percobaan. Angka yang benar adalah {angka_rahasia}.")

# Memulai permainan
tebak_angka()
