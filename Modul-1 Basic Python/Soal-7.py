def min_coin_change(coins, jumlah_uang):
    # Inisialisasi array untuk menyimpan jumlah minimum koin yang diperlukan untuk setiap nilai
    # Gunakan nilai yang besar (float('inf')) sebagai penanda bahwa belum ada solusi yang ditemukan
    dp = [float('inf')] * (jumlah_uang + 1)
    
    # Untuk jumlah uang 0, jumlah koin yang diperlukan adalah 0
    dp[0] = 0
    
    # Iterasi untuk setiap jumlah uang dari 1 hingga jumlah_uang
    for uang in range(1, jumlah_uang + 1):
        for coin in coins:
            if uang >= coin:
                dp[uang] = min(dp[uang], dp[uang - coin] + 1)
    
    # Jika jumlah uang tidak bisa dicapai, kembalikan -1
    return dp[jumlah_uang] if dp[jumlah_uang] != float('inf') else -1

def hitung_koin_minimum():
    try:
        # Meminta input jumlah uang
        jumlah_uang = int(input("Masukkan jumlah uang: "))
        
        # Meminta input daftar koin
        koin_input = input("Masukkan nilai koin yang tersedia (pisahkan dengan spasi): ")
        coins = list(map(int, koin_input.split()))

        # Panggil fungsi untuk menghitung minimum koin
        hasil = min_coin_change(coins, jumlah_uang)
        
        if hasil == -1:
            print(f"Tidak ada kombinasi koin yang dapat mencapai jumlah uang {jumlah_uang}.")
        else:
            print(f"Jumlah minimum koin yang diperlukan untuk mencapai {jumlah_uang}: {hasil}")
    
    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan bilangan bulat.")

# Jalankan program
hitung_koin_minimum()