# Bilangan Ganjil dan Genap
Angka = int(input("Masukan Bilangan Bulat:"))

if Angka % 2 == 0:
 print("Bilangan Genap")
else:
 print("Bilangan Ganjil")


#  Nilai Ujian
Nilai = int(input("Masukan Nilai: "))

if Nilai >= 75:
 print("Lulus")
else :
 print("Tidak Lulus")


# Cek Usia dan Status
Usia = int(input("Masukan Usia: "))

if Usia >= 18:
 print("Dewasa")
elif Usia < 18 and Usia >= 13:
 print ("Remaja")
else :
  print ("Anak-Anak")


# Cek Keanggotaan
Status = input("Masukan Status Keanggotaan: ")

if Status == "Gold" or Status == "Silver" :
 print("Selamat! Anda mendapatkat diskon")
elif Status == "Bronze" :
 print("Silahkan tingkatkan status keanggotaan anda :)")
else :
 print("Status tidak valid")


# Pembelian Diskon
Jumlah_pembelian = int(input("Masukan Jumalah Pembelian: "))
Harga_item = 100

Harga_diskon = Harga_item * Jumlah_pembelian * (10/100)
Harga_total = Harga_item * Jumlah_pembelian
Total = Harga_total - Harga_diskon

print(f"Selamat! anda mendapatkan potongan harga sebanyak 10%, Harga per item {Harga_item}, Jadi Total harga yang harus anda bayar saat ini adalah {Total}") if Jumlah_pembelian > 100 else print(f"Harga per item {Harga_item}, Jadi total harga yang harus dibayar adalah {Harga_total}")
