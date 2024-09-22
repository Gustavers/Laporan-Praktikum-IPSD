def pencarian_biner(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  

def main():
    # Daftar angka genap
    angka_genap = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    # Meminta input dari pengguna
    try:
        target = int(input("Masukkan angka yang ingin dicari: "))
        
        if target % 2 != 0:  # Cek apakah angka ganjil
            print("Nilai tidak bisa ditemukan karena nilai yang dicari adalah angka ganjil.")
            return
        
        # Melakukan pencarian biner
        hasil = pencarian_biner(angka_genap, target)
        
        if hasil != -1:
            print(f"Angka {target} ditemukan di indeks {hasil}.")
        else:
            print(f"Angka {target} tidak ditemukan dalam daftar.")
    
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat.")

# Menjalankan program
main()
