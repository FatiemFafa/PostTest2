from prettytable import PrettyTable
import os

daftar = {
    "pemeriksaan"  : ["Pemeriksaan Darah"],
    "harga": [10000]
}

table = PrettyTable()
table.title = 'LAB KESEHATAN'
table.field_names = ["No","Pemeriksaan","Harga"]

def tables():
    table.clear_rows()
    if len(daftar['pemeriksaan']) <= 0:
        print("Data Kosong")
    else:
        for i in range(len(daftar['pemeriksaan'])):
            table.add_row([i + 1,daftar['pemeriksaan'][i],daftar['harga'][i]])
        print(table)

def ulang():
    ulang = input("Apakah anda ingin mengulang ya / tidak : ")
    if ulang.lower() == "ya" or ulang.lower() == "y" :
        admin()
    else: exit()

def admin():
    print("Selamat Datang Admin") 
    print("1. Liat Daftar Kesehatan")
    print("2. Tambah Daftar Kesehatan")
    print("3. Edit Daftar Kesehatan")
    print("4. Hapus Daftar Kesehatan")
    print("5. Logout")
    pilih = input("Masukan Pilihan Menu : ")
    while True:
        if pilih == "1":
            os.system('cls')
            tables()
            ulang()
        elif pilih == "2":
            os.system('cls')
            tables()
            pemeriksaanBaru = input("Masukan Nama Pemeriksaan : ")
            hargaBaru = int(input("Masukan Harga Baru : "))
            if pemeriksaanBaru in daftar['pemeriksaan']:
                os.system('cls')
                print("Nama Pemeriksaan Sudah ada")
                ulang()
            else:
                daftar['pemeriksaan'].append(pemeriksaanBaru)
                daftar['harga'].append(hargaBaru)
                tables()
                print("Data Berhasil Ditambahkan")
                ulang()
        elif pilih == "3":
            os.system('cls')
            tables()
            pilih = int(input("Masukan Nomor Pilihan Anda : "))
            pilih  -= 1
            os.system('cls')
            print("Anda mengedit data : ",daftar['pemeriksaan'][pilih])
            pemeriksaanBaru = input("Masukan Nama Pemeriksaan Baru : ")
            hargaBaru = int(input("Masukan Harga Baru : "))
            daftar['pemeriksaan'][pilih] = pemeriksaanBaru
            daftar['harga'][pilih] = hargaBaru 
            tables() 
            ulang()
        elif pilih == "4":
            os.system('cls')
            tables()
            pilih = int(input("Masukan Nomor Pilihan Anda Yang Ingin Dihapus: "))
            pilih -=1 
            daftar.get('pemeriksaan').pop(pilih)
            daftar.get('harga').pop(pilih)
            ulang()
        elif pilih == "5":
            main()
        else:
            os.system('cls')
            admin()

def pasien():
    pilih = input("Apakah Anda Ingin Membeli? ya / tidak : ")
    if pilih.lower() == "ya" or pilih.lower() == "y":
        pilihan = int(input("Nomor Yang Ingin Dibook: "))
        pilihan -=1
        print("Anda Membooking : ",daftar['pemeriksaan'][pilihan])
        print("Harga : ",daftar['harga'][pilihan])
        print("Berhasil Membook")
        pasien()
    else:
        print("1.Logout")
        print("2.Exit")
        pilih = input("Masukan Pilihan: ")
        if pilih == "1":
            main()
        else:exit()

def main():
    print("Masukan Role Anda")
    print("1.Admin")
    print("2.Pasien")
    role = input("Pilih Role Anda -> ")
    if role == "1":
        nama = input("Masukan Nama Anda: ")
        password = input("Masukan Password Anda: ")
        if nama == "admin" and password == "admin":
            os.system('cls')
            admin()
    elif role == "2":
        tables()
        pasien()
    else:print("Invalid")

main()