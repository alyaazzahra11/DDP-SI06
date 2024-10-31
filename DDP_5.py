
# Buat variabel list
list = ["Mobil", "Kendaraan Beroda Empat", 2.477, "Putih", "Beroda empat"]
print(list)

list.append (767200000)
print(list)

list.append ("Tipe Pajero Sport Exceed")
print(list)

list.insert(2, "Mitsubishi Pajero Sport")
print(list)

# Buat program python dengan match case
luas_bangun_datar = int(input("""Selamat datang diaplikasi menghitung
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran
3. Untuk menghitung luas segitiga 

Masukan pilihan anda"""))

match luas_bangun_datar :
    case 1 :
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("Masukan sisi persegi : "))
        Luas_persegi = sisi*sisi
        print("Hasil luas persegi dengan sisi", sisi, "adalah", Luas_persegi)
    
    case 2 :
        print("Kamu memilih 2 untuk menghitung luas lingkaran")
        jarijari = int(input("Masukan jari-jari lingkaran : "))
        Luas_lingkaran = 3.14 * jarijari * jarijari
        print("Hasil luas lingkaran dengan jari-jari", jarijari, "adalah", Luas_lingkaran)
    
    case 3 :
        print("Kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("Masukan alas segitiga : "))
        tinggi = int(input("Masukan tinggi segitiga : "))
        Luas_segitiga = 0.5 * alas * tinggi
        print("Hasil luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", Luas_segitiga)

    case _ :
        print("Anda salah pilih")
