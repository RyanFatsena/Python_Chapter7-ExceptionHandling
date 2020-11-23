# Praktikum 2 Nomor 5

try:
    # membuka dan mau membaca file Dokumen:/data1.txt
    file = open("iCloud Drive:/data1.txt", "r")

    # baca baris pertama dari file
    # simpan ke dalam variabel bil1 sbg integer
    bil1 = int(file.readline())

    # baca baris pertama dari file
    # simpan ke dalam variabel bil2 sbg integer
    bil2 = int(file.readline())

    # hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1, 'dibagi', bil2, '=', hasil)

except FileNotFoundError:
    print("File tidak ditemukan")

except ZeroDivisionError:
    print("Tidak boleh pembagian dengan nol")
