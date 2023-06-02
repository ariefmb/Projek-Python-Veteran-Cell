# Library
from datetime import datetime
now = datetime.now()
tanggal = now.strftime ("%d/%m/%Y")
kode_trans = now.strftime ("VTRN/%f%H%M%S")

import os

# Membuat Dictionary
pulsa = {
    "5k" : 7000,
    "10k" : 12000,
    "20k" : 22000,
    "50k" : 52000,
    "100k" : 102000,
    "500k" : 502000
}

paket_data = {
    "1gb" : 11500,
    "5gb" : 41500,
    "10gb" : 70000,
    "25gb" : 100000,
    "50gb" : 145000,
    "100gb" : 265000
}

token_listrik = {
    "13kwh" : 20000,
    "33kwh" : 50000,
    "66kwh" : 100000,
    "132kwh" : 250000,
    "328kwh" : 500000,
    "659kwh" : 1000000
}

gopay = {
    "20k" : 22000,
    "50k" : 52000,
    "100k" : 102000,
    "500k" : 502000,
    "1jt" : 1002000
}

dana = {
    "10k" : 12000,
    "20k" : 22000,
    "50k" : 52000,
    "100k" : 102000,
    "500k" : 502000
}

ovo = {
    "10k" : 12000,
    "20k" : 22000,
    "50k" : 52000,
    "100k" : 102000,
    "500k" : 502000,
    "1jt" : 1002000
}

transfer_bank = {
    "50k" : 57500,
    "100k" : 107500,
    "200k" : 207500,
    "300k" : 307500,
    "400k" : 407500,
    "500k" : 507500,
    "1jt" : 1007500
}

voucher_belanja = {
    "50k" : 50000,
    "100k" : 100000,
    "250k" : 250000,
    "500k" : 500000,
    "750k" : 750000,
    "1jt" : 1000000
}

# Membuat list untuk menampung daftar dan total belanja
list_harga      = []
list_belanja    = []

# Membuat function
def hargapulsa():
    print("==============================================")
    print("==========        HARGA PULSA       ==========")
    print("==============================================")
    print("Nominal               |   Harga      ")
    print("==============================================")
    print("5k                    |   7.000")
    print("10k                   |   12.000")
    print("20k                   |   22.000")
    print("50k                   |   52.000")
    print("100k                  |   102.000")
    print("500k                  |   502.000")
    print("==============================================")
    input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")

def hargapaketdata():
    print("==============================================")
    print("=========      HARGA PAKET DATA      =========")
    print("==============================================")
    print("Nominal                |   Harga      ")
    print("==============================================")
    print("1gb                    |   11.500")
    print("5gb                    |   41.500")
    print("10gb                   |   70.000")
    print("25gb                   |   100.000")
    print("50gb                   |   145.000")
    print("100gb                  |   265.000")
    print("==============================================")
    input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")

def hargatokenlistrik():
    print("==============================================")
    print("========      HARGA TOKEN LISTRIK     ========")
    print("==============================================")
    print("Nominal                |   Harga      ")
    print("==============================================")
    print("13kwh                  |   20.000")
    print("33kwh                  |   50.000")
    print("66kwh                  |   100.000")
    print("132kwh                 |   250.000")
    print("328kwh                 |   500.000")
    print("659kwh                 |   1.000.000")
    print("==============================================")
    input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")

def hargagopay():
    print("==============================================")
    print("========       HARGA SALDO GOPAY      ========")
    print("==============================================")
    print("Nominal               |   Harga      ")
    print("==============================================")
    print("20k                   |   22.000")
    print("50k                   |   52.000")
    print("100k                  |   102.000")
    print("500k                  |   502.000")
    print("1jt                   |   1.002.000")
    print("==============================================")
    input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")

def hargadana():
    print("==============================================")
    print("========       HARGA SALDO DANA       ========")
    print("==============================================")
    print("Nominal               |   Harga      ")
    print("==============================================")
    print("10k                   |   12.000")
    print("20k                   |   22.000")
    print("50k                   |   52.000")
    print("100k                  |   102.000")
    print("500k                  |   502.000")
    print("==============================================")
    input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")

def hargaovo():
    print("==============================================")
    print("========        HARGA SALDO OVO       ========")
    print("==============================================")
    print("Nominal                |   Harga      ")
    print("==============================================")
    print("10k                    |   12.000")
    print("20k                    |   22.000")
    print("50k                    |   52.000")
    print("100k                   |   102.000")
    print("500k                   |   502.000")
    print("1jt                    |   1.002.000")
    print("==============================================")
    input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")

def biayatfbank():
    print("==============================================")
    print("=======       HARGA TRANSFER BANK      =======")
    print("==============================================")
    print("Nominal                 |   Harga      ")
    print("==============================================")
    print("50k                     |   57.500")
    print("100k                    |   107.500")
    print("200k                    |   207.500")
    print("300k                    |   307.500")
    print("400k                    |   407.500")
    print("500k                    |   507.500")
    print("1jt                     |   1.007.500")
    print("==============================================")
    input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")

def hargavocbelanja():
    print("==============================================")
    print("=======      HARGA VOUCHER BELANJA     =======")
    print("==============================================")
    print("Nominal                 |   Harga      ")
    print("==============================================")
    print("50k                     |   50.000")
    print("100k                    |   100.000")
    print("250k                    |   250.000")
    print("500k                    |   500.000")
    print("750k                    |   750.000")
    print("1jt                     |   1.000.000")
    print("==============================================")
    input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")

def fpulsa():
    print("\n=======   FORM PEMBELIAN PULSA     =======\n")
    Nama = input("Nama Customer \t: ")
    Hp = input("No. HP \t\t: ")
    Nom = input("Nominal Pembelian (5k | 10k | 20k | 50k | 100k | 500k) \n=> Masukkan sesuai nominal: ")
    Harga = pulsa[Nom]
    print("==============================================")
    user_conf = input("Apakah anda yakin ingin membelinya? (Y/N) \n=> Masukkan pilihan anda: ").upper()
    if (user_conf == "Y"):
        list_harga.append(Harga)
        list_belanja.append(f"Pulsa \t\t\t{Nom} \t: Rp {Harga}")
        print("==============================================")
        user_conf = int(input("1. Cetak Data Pembelian \n2. Kembali ke Menu Utama \n\n=> Masukkan pilihan anda: "))
        os.system("cls")
        if (user_conf == 1):
            print("\n==============================================")
            print("VETERAN CELL | NOTA PEMBELIAN | PULSA\n\nKode Transaksi\t\t: ",kode_trans, "\nTanggal Pembelian\t: ",tanggal,"\nNama Customer\t\t: ",Nama,"\nNo. HP\t\t\t: ",Hp,"\n\nNominal Pembelian\t: ",Nom,"\n\nHarga\t\t\t:  Rp",Harga)
            print("\nSILAHKAN LAKUKAN PEMBAYARAN DI MENU PEMBAYARAN")
            print("==============================================\n")
            input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
        else:
            print("==============================================")
    else:
        print("==============================================")

def fpaketdata():
    print("\n=======   FORM PEMBELIAN PAKET DATA     =======\n")
    Nama = input("Nama Customer \t: ")
    Hp = input("No. HP \t\t: ")
    Nom = input("Nominal Pembelian (1gb | 5gb | 10gb | 25gb | 50gb | 100gb) \n=> Masukkan sesuai nominal: ")
    Harga = paket_data[Nom]
    print("==============================================")
    user_conf = input("Apakah anda yakin ingin membelinya? (Y/N) \n=> Masukkan pilihan anda: ").upper()
    if (user_conf == "Y"):
        list_harga.append(Harga)
        list_belanja.append(f"Paket Data \t\t{Nom} \t: Rp {Harga}")
        print("==============================================")
        user_conf = int(input("1. Cetak Data Pembelian \n2. Kembali ke Menu Utama \n\n=> Masukkan pilihan anda: "))
        os.system("cls")
        if (user_conf == 1):
            print("\n==============================================")
            print("VETERAN CELL | NOTA PEMBELIAN | PAKET DATA\n\nKode Transaksi\t\t: ",kode_trans, "\nTanggal Pembelian\t: ",tanggal,"\nNama Customer\t\t: ",Nama,"\nNo. HP\t\t\t: ",Hp,"\n\nNominal Pembelian\t: ",Nom,"\n\nHarga\t\t\t:  Rp",Harga)
            print("\nSILAHKAN LAKUKAN PEMBAYARAN DI MENU PEMBAYARAN")
            print("==============================================\n")
            input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
        else:
            print("==============================================")
    else:
        print("==============================================")

def ftokenlistrik():
    print("\n=======   FORM PEMBELIAN TOKEN LISTRIK     =======\n")
    Nama = input("Nama Customer\t\t: ")
    wa = input("No. Whatsapp untuk menerima Kode Token : ")
    Nom = input("Nominal Pembelian (13kwh | 33kwh | 66kwh | 132kwh | 328kwh | 659kwh) \n=> Masukkan sesuai nominal: ")
    Harga = token_listrik[Nom]
    print("==============================================")
    user_conf = input("Apakah anda yakin ingin membelinya? (Y/N) \n=> Masukkan pilihan anda: ").upper()
    if (user_conf == "Y"):
        list_harga.append(Harga)
        list_belanja.append(f"Token Listrik \t\t{Nom} \t: Rp {Harga}")
        print("==============================================")
        user_conf = int(input("1. Cetak Data Pembelian \n2. Kembali ke Menu Utama \n\n=> Masukkan pilihan anda: "))
        os.system("cls")
        if (user_conf == 1):
            print("\n==============================================")
            print("VETERAN CELL | NOTA PEMBELIAN | TOKEN LISTRIK\n\nKode Transaksi\t\t: ",kode_trans, "\nTanggal Pembelian\t: ",tanggal,"\nNama Customer\t\t: ",Nama,"\nNo. Whatsapp\t\t: ",wa,"\n\nNominal Pembelian\t: ",Nom,"\n\nHarga\t\t\t:  Rp",Harga)
            print("\nSILAHKAN LAKUKAN PEMBAYARAN DI MENU PEMBAYARAN")
            print("==============================================\n")
            input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
        else:
            print("==============================================")
    else:
        print("==============================================")

def fgopay():
    print("\n=======   FORM PEMBELIAN SALDO GOPAY     =======\n")
    Nama = input("Nama Customer \t: ")
    No_gopay = input("No. Gopay \t: ")
    Nom = input("Nominal Pembelian (20k | 50k | 100k | 500k | 1jt) \n=> Masukkan sesuai nominal: ")
    Harga = gopay[Nom]
    print("==============================================")
    user_conf = input("Apakah anda yakin ingin membelinya? (Y/N) \n=> Masukkan pilihan anda: ").upper()
    if (user_conf == "Y"):
        list_harga.append(Harga)
        list_belanja.append(f"Gopay \t\t\t{Nom} \t: Rp {Harga}")
        print("==============================================")
        user_conf = int(input("1. Cetak Data Pembelian \n2. Kembali ke Menu Utama \n\n=> Masukkan pilihan anda: "))
        os.system("cls")
        if (user_conf == 1):
            print("\n==============================================")
            print("VETERAN CELL | NOTA PEMBELIAN | SALDO GOPAY\n\nKode Transaksi\t\t: ",kode_trans, "\nTanggal Pembelian\t: ",tanggal,"\nNama Customer\t\t: ",Nama,"\nNo. Gopay\t\t: ",No_gopay,"\n\nNominal Pembelian\t: ",Nom,"\n\nHarga\t\t\t:  Rp",Harga)
            print("\nSILAHKAN LAKUKAN PEMBAYARAN DI MENU PEMBAYARAN")
            print("==============================================\n")
            input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
        else:
            print("==============================================")
    else:
        print("==============================================")

def fdana():
    print("\n=======   FORM PEMBELIAN SALDO DANA     =======\n")
    Nama = input("Nama Customer \t: ")
    No_dana = input("No. Dana \t: ")
    Nom = input("Nominal Pembelian (10k | 20k | 50k | 100k | 500k) \n=> Masukkan sesuai nominal: ")
    Harga = dana[Nom]
    print("==============================================")
    user_conf = input("Apakah anda yakin ingin membelinya? (Y/N) \n=> Masukkan pilihan anda: ").upper()
    if (user_conf == "Y"):
        list_harga.append(Harga)
        list_belanja.append(f"Dana \t\t\t{Nom} \t: Rp {Harga}")
        print("==============================================")
        user_conf = int(input("1. Cetak Data Pembelian \n2. Kembali ke Menu Utama \n\n=> Masukkan pilihan anda: "))
        os.system("cls")
        if (user_conf == 1):
            print("\n==============================================")
            print("VETERAN CELL | NOTA PEMBELIAN | SALDO DANA\n\nKode Transaksi\t\t: ",kode_trans, "\nTanggal Pembelian\t: ",tanggal,"\nNama Customer\t\t: ",Nama,"\nNo. Dana\t\t: ",No_dana,"\n\nNominal Pembelian\t: ",Nom,"\n\nHarga\t\t\t:  Rp",Harga)
            print("\nSILAHKAN LAKUKAN PEMBAYARAN DI MENU PEMBAYARAN")
            print("==============================================\n")
            input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
        else:
            print("==============================================")
    else:
        print("==============================================")

def fovo():
    print("\n=======   FORM PEMBELIAN SALDO OVO     =======\n")
    Nama = input("Nama Customer \t: ")
    No_ovo = input("No. Ovo \t: ")
    Nom = input("Nominal Pembelian (10k | 20k | 50k | 100k | 500k | 1jt) \n=> Masukkan sesuai nominal: ")
    Harga = ovo[Nom]
    print("==============================================")
    user_conf = input("Apakah anda yakin ingin membelinya? (Y/N) \n=> Masukkan pilihan anda: ").upper()
    if (user_conf == "Y"):
        list_harga.append(Harga)
        list_belanja.append(f"Ovo \t\t\t{Nom} \t: Rp {Harga}")
        print("==============================================")
        user_conf = int(input("1. Cetak Data Pembelian \n2. Kembali ke Menu Utama \n\n=> Masukkan pilihan anda: "))
        os.system("cls")
        if (user_conf == 1):
            print("\n==============================================")
            print("VETERAN CELL | NOTA PEMBELIAN | SALDO OVO\n\nKode Transaksi\t\t: ",kode_trans, "\nTanggal Pembelian\t: ",tanggal,"\nNama Customer\t\t: ",Nama,"\nNo. Ovo\t\t\t: ",No_ovo,"\n\nNominal Pembelian\t: ",Nom,"\n\nHarga\t\t\t:  Rp",Harga)
            print("\nSILAHKAN LAKUKAN PEMBAYARAN DI MENU PEMBAYARAN")
            print("==============================================\n")
            input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
        else:
            print("==============================================")
    else:
        print("==============================================")

def ftfbank():
    print("\n=======   FORM TRANSFER BANK     =======\n")
    Nama = input("Nama Customer \t\t: ")
    No_rek = input("No. Rekening tujuan \t: ")
    Nom = input("Nominal Transfer (50k | 100k | 200k | 300k | 400k | 500k | 1jt) \n=> Masukkan sesuai nominal: ")
    Harga = transfer_bank[Nom]
    print("==============================================")
    user_conf = input("Apakah anda yakin ingin membelinya? (Y/N) \n=> Masukkan pilihan anda: ").upper()
    if (user_conf == "Y"):
        list_harga.append(Harga)
        list_belanja.append(f"Transfer Bank \t\t{Nom} \t: Rp {Harga}")
        print("==============================================")
        user_conf = int(input("1. Cetak Data Pembelian \n2. Kembali ke Menu Utama \n\n=> Masukkan pilihan anda: "))
        os.system("cls")
        if (user_conf == 1):
            print("\n==============================================")
            print("VETERAN CELL | NOTA PEMBELIAN | TRANSFER BANK \n\nKode Transaksi\t\t: ",kode_trans, "\nTanggal Pembelian\t: ",tanggal,"\nNama Customer\t\t: ",Nama,"\nNo. Rekening\t\t: ",No_rek,"\n\nNominal Pembelian\t: ",Nom,"\n\nHarga\t\t\t:  Rp",Harga)
            print("\nSILAHKAN LAKUKAN PEMBAYARAN DI MENU PEMBAYARAN")
            print("==============================================\n")
            input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
        else:
            print("==============================================")
    else:
        print("==============================================")

def fvocbelanja():
    print("\n=======   FORM PEMBELIAN VOUCHER BELANJA     =======\n")
    Nama = input("Nama Customer \t\t: ")
    email = input("Email untuk menerima voucher digital\t: ")
    Nom = input("Nominal Pembelian (50k | 100k | 250k | 500k | 750k | 1jt) \n=> Masukkan sesuai nominal: ")
    Harga = voucher_belanja[Nom]
    print("==============================================")
    user_conf = input("Apakah anda yakin ingin membelinya? (Y/N) \n=> Masukkan pilihan anda: ").upper()
    if (user_conf == "Y"):
        list_harga.append(Harga)
        list_belanja.append(f"Voucher Belanja \t{Nom} \t: Rp {Harga}")
        print("==============================================")
        user_conf = int(input("1. Cetak Data Pembelian \n2. Kembali ke Menu Utama \n\n=> Masukkan pilihan anda: "))
        os.system("cls")
        if (user_conf == 1):
            print("\n==============================================")
            print("VETERAN CELL | NOTA PEMBELIAN | VOUCHER BELANJA \n\nKode Transaksi\t\t: ",kode_trans, "\nTanggal Pembelian\t: ",tanggal,"\nNama Customer\t\t: ",Nama,"\nEmail\t\t\t: ",email,"\n\nNominal Pembelian\t: ",Nom,"\n\nHarga\t\t\t:  Rp",Harga)
            print("\nSILAHKAN LAKUKAN PEMBAYARAN DI MENU PEMBAYARAN")
            print("==============================================\n")
            input("\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
        else:
            print("==============================================")
    else:
        print("==============================================")

def pembayaran():
    while True:
        total_belanja = sum(list_harga)
        print(f"\nTOTAL \t\t\t\t: Rp {total_belanja}")
        uang_bayar = int(input("Masukkan uang Anda\t\t: Rp "))
        kembalian = uang_bayar - total_belanja
        user_conf = input("Apakah anda ingin melanjutkan pembayaran? (Y/N) \n=> Masukkan pilihan anda: ").upper()
        os.system("cls")
        
        if user_conf == "Y":
            if uang_bayar < total_belanja:
                print("===============================================")
                print("=========     PEMBAYARAN KURANG      ==========")
                print("===============================================")
                input("\n\x1B[3mKetuk Enter untuk Kembali Membayar \x1B[0m")
            else:
                print("==============================================")
                print("        VETERAN CELL | STRUK PEMBELIAN")
                print("==============================================")
                print(f"Kode Struk        :          {kode_trans}")
                print(f"Tanggal Transaksi :                 {tanggal}")
                print("==============================================")
                print("BARANG                  JENIS     HARGA\n")
                for i in list_belanja:
                    print(i)
                print("==============================================")
                print(f"TOTAL \t\t\t\t: Rp {total_belanja}")
                print(f"TUNAI \t\t\t\t: Rp {uang_bayar}")
                print(f"KEMBALIAN \t\t\t: Rp {kembalian}")
                print("==============================================")
                print("=========       TERIMA KASIH        ==========")
                print("==============================================")
                return input("\n\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
        else:
            return
        
def sequential_search(menu, produk):
    start = 0
    temp = False
    while start < len(menu) and not temp:
        if menu[start] == produk:
            os.system("cls")
            temp = True
            return input(f"\nYapss, kami menyediakan {produk} \n\n\n\x1B[3mKetuk Enter untuk Kembali ke Menu\x1B[0m")
        else:
            start += 1
    return input(f"\nMaaf, kami tidak menjual {produk} \n\n\n\x1B[3mKetuk Enter untuk Kembali ke Menu \x1B[0m")
    
def search_produk():
    while True:
        os.system("cls")
        print("==============================================")
        print("VETERAN CELL          |         MENU PENCARIAN")
        print("==============================================\n")
        produk = ["pulsa", "paket data","paketdata", "token listrik","tokenlistrik", "gopay", "dana", "ovo", "transfer bank","tf bank", "voucher belanja","voc belanja"]
        print("99. Kembali ke Menu\n")
        print("Anda sedang mencari produk apa?")
        user_searching = input("Search: ")
        os.system("cls")

        if user_searching == "99":
            break
        else:
            sequential_search(produk, user_searching)

def katalog():
    while True:
        os.system("cls")
        print("===============================================================")
        print("VETERAN CELL | melayani berbagai macam pembelian produk digital")
        print("===============================================================")
        print("Pulsa      | Paket Data | Token Listrik | Saldo Gopay")
        print("Saldo Dana | Saldo Ovo  | Transfer Bank | Voucher Belanja")
        print("==============================================")
        print("1. Cek Harga Pulsa\n2. Cek Harga Paket Data\n3. Cek Harga Token Listrik\n4. Cek Harga Saldo Gopay\n5. Cek Harga Saldo Dana\n6. Cek Harga Saldo Ovo\n7. Cek Biaya Transfer Bank\n8. Cek Harga Voucher Belanja\n9. Kembali ke Menu")
        print("==============================================")
        user_cekharga = int(input("Masukkan Angka Sesuai Pilihan di Atas: "))
        os.system("cls")

        if (user_cekharga == 1):
            hargapulsa()
        elif (user_cekharga == 2):
            hargapaketdata()
        elif (user_cekharga == 3):
            hargatokenlistrik()
        elif (user_cekharga == 4):
            hargagopay()
        elif (user_cekharga == 5):
            hargadana()
        elif (user_cekharga == 6):
            hargaovo()
        elif (user_cekharga == 7):
            biayatfbank()
        elif (user_cekharga == 8):
            hargavocbelanja()
        else:
            return

# Program Utama
while True:
    os.system("cls")
    print("==============================================")
    print(">>>>>>    Konter Pulsa Veteran Cell    <<<<<<<\n\n1.  Katalog Produk\n2.  Pencarian Produk \n3.  Beli Pulsa\n4.  Beli Paket Data\n5.  Beli Token Listrik\n6.  Beli Saldo Gopay")
    print("7.  Beli Saldo Dana\n8.  Beli Saldo Ovo\n9.  Transfer Uang ke Seluruh Bank\n10. Beli Voucher Belanja\n11. Keluar\n\n99. Menu Pembayaran / Kasir\n")
    print("==============================================")
    user_menu = int(input("Masukkan angka sesuai pilihan di atas: "))
    os.system("cls")
    print("==============================================")

    if (user_menu == 1):
        katalog()
    elif (user_menu == 2):
        search_produk()
    elif (user_menu == 3):
        fpulsa()
    elif (user_menu == 4):
        fpaketdata()
    elif (user_menu == 5):
        ftokenlistrik()
    elif (user_menu == 6):
        fgopay()
    elif (user_menu == 7):
        fdana()
    elif (user_menu == 8):
        fovo()
    elif (user_menu == 9):
        ftfbank()
    elif (user_menu == 10):
        fvocbelanja()
    elif (user_menu == 99):
        pembayaran()
    else:
        print("==============================================")
        print("===     Terima Kasih Telah Berkunjung      ===")
        print("==============================================")
        exit()

# Notes
# \n        ini adalah notasi untuk membuat line baru
# \t        ini adalah notasi untuk tab 
# \x1B[3m   ini adalah notasi untuk membuat text menjadi italic
# \x1B[0m   ini adalah notasi untuk mengembalikan text menjadi normal