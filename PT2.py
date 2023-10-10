import os
os.system("cls")

from prettytable import PrettyTable

#PrettyTable
dataHelm = [
    [1, "Helm Fullface RSV", 500000],
    [2, "Helm fullface INK", 350000],
    [3, "Helm Pogo Cargloss", 250000],
    [4, "Helm Pogo Classic", 200000],
    [5, "Helm Standar NHK", 150000],
    [6, "Helm fullface KYT", 125000],
]

produklaku =[]

#pemilihan role
def role() :
    while True :
        pilihrole = str(input("Apa role anda?\n1. Pelanggan\n2. Admin\nPilihan anda: "))
        if pilihrole == "1" :
            pelanggan()
            break
        elif pilihrole == "2":
            admin()
            break
        else :
            print("Pilihan tidak valid. Pilih role yang ada.")

#User dan menu admin
def admin() :
    while True :
        print("\nPilihan Menu Admin:")
        print("1. Tampilkan Helm")
        print("2. Tambah Helm Baru")
        print("3. Perbarui Tabel Helm")
        print("4. Hapus Helm dari Tabel")
        print("5. Exit")
        
        pilihan = int(input("Pilih Nomor Menu: "))
        if pilihan == 1:
            tampilkan()
        elif pilihan == 2:
            create()
        elif pilihan == 3:
            update()
        elif pilihan == 4:
            delete()
        elif pilihan == 5:
            break
        else :
            print("Pilihan tidak valid. Menu pilihan tidak tersedia.")

#User pelanggan
def pelanggan():
        tampilkan()
        noProduk = int(input('Masukkan nomor produk yang ingin dibeli:  '))
        if noProduk == 1:
            print("Produk yang anda beli yaitu Helm Fullface RSV = Rp. 500000")
        elif noProduk == 2:
            print("Produk yang anda beli yaitu Helm fullface INK = Rp. 350000")
        elif noProduk == 3:
            print("Produk yang anda beli yaitu Helm Pogo Cargloss = 250000")
        elif noProduk == 4:
            print("Produk yang anda beli yaitu Helm Pogo Classic = 200000")
        elif noProduk == 5:
            print("Produk yang anda beli yaitu Helm Standar NHK = 150000")
        elif noProduk == 6:
            print("Produk yang anda beli yaitu Helm standar KYT = 120000")
        else:
            print("Produk yang anda pilih tidak ada")


#create
def create() :
    tampilkan()
    nomor = int(input("Masukan Nomor Helm yang baru : "))

    for noHelm in dataHelm:
        if noHelm [0] == nomor:
            print(f"Produk dengan nomor {nomor} sudah ada.")
            return
        
    namaHelm = str(input("Masukkan Nama Helm : "))
    hargaHelm = int(input("Masukkan Harga Helm : "))
    dataHelm.append([nomor, namaHelm, hargaHelm])
    tampilkan()
    print("\nHelm baru berhasil ditambahkan")

#read
def tampilkan() :
    tabelDataHelm = PrettyTable(["No.", "Nama Helm", "Harga Helm"])
    for barisData in dataHelm :
        tabelDataHelm.add_row(barisData)

    print(tabelDataHelm)

#update
def update() :
    tampilkan()
    noBaru = int(input("Masukan nomor yang ingin di update : "))
    for barisData in dataHelm :

        if barisData [0] == noBaru :
            helmBaru = str(input("Masukkan Nama Helm yang baru : "))
            hargaBaru = int(input("Masukkan Harga Helm yang baru : "))
            barisData[1] = helmBaru
            barisData[2] = hargaBaru
            tampilkan()
            print("Produk berhasil diperbarui")
            return
    print("Nomor barang tidak ditemukan")

#delete
def delete() :
    tampilkan()
    Hapus = int(input("Masukan nomor Helm yang ingin dihapus: "))
    for barisData in dataHelm:
        if barisData[0] == Hapus:
            dataHelm.remove(barisData)
            tampilkan()
            print("Helm berhasil dihapus")
            return
    print("Nomor barang tidak ditemukan")
role()