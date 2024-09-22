# Program Simulasi ATM
def mesin_atm():
    # Set PIN 
    correct_pin = "1234"
    saldo = 1000000  # saldo awal
    max_attempts = 3

    # meminta pengguna memasukkan pin max 3 percobaan
    attempts = 0
    while attempts < max_attempts:
        pin_input = input("Masukkan PIN ATM: ")
        if pin_input == correct_pin:
            print("PIN benar.")
            break
        else:
            attempts += 1
            print(f"PIN salah. Percobaan tersisa: {max_attempts - attempts}")
    
    # Jika PIN salah 3 kali, keluarkan dari program
    if attempts == max_attempts:
        print("Anda telah gagal memasukkan PIN 3 kali. Kartu ATM diblokir.")
        return

    # Meminta jumlah penarikan
    while True:
        try:
            penarikan = int(input("Masukkan jumlah penarikan: "))
            if penarikan <= 0:
                print("Jumlah penarikan harus lebih dari 0.")
                continue
        except ValueError:
            print("Masukkan jumlah penarikan yang valid.")
            continue

        # Periksa saldo cukup atau tidak
        if penarikan > saldo:
            print("Saldo tidak mencukupi untuk melakukan penarikan.")
        else:
            # penarikan dan menampilkan saldo
            saldo -= penarikan
            print(f"Penarikan berhasil. Sisa saldo Anda: Rp {saldo:,}")
            break

mesin_atm()
