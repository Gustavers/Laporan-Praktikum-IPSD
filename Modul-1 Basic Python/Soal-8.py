def kata_terbalik(input_string):
    # Memisahkan string menjadi kata-kata
    kata_list = input_string.split()
    
    # Membalik setiap kata dalam list
    kata_terbalik = [kata[::-1] for kata in kata_list]
    
    return kata_terbalik

def main():
    # Menerima input dari pengguna
    input_string = input("Masukkan sebuah kalimat: ")
    
    # Mengonversi menjadi list kata terbalik
    hasil = kata_terbalik(input_string)
    
    # Menampilkan hasil
    print("Output:", hasil)

# Menjalankan program
main()
