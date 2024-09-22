def kombinasi(list1, list2):
    # Mengambil elemen dengan indeks ganjil dari kedua list
    index_ganjil = [list1[i] for i in range(len(list1)) if i % 2 == 1] + \
                    [list2[i] for i in range(len(list2)) if i % 2 == 1]
    
    # Mengurutkan elemen secara menurun
    index_ganjil.sort(reverse=True)
    return index_ganjil

# Contoh 
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
hasil = kombinasi(list_a, list_b)
print(hasil)  
