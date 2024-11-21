# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
print("----- No 1 -----")
def celcius_to_fahrenheit (celcius):
    print((9/5 * celcius) + 32)

celcius_to_fahrenheit(0)
celcius_to_fahrenheit(100)

#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
print("----- No 2 -----")
def is_genap (angka):
    print(angka % 2 == 0)

is_genap(4)
is_genap(7)

#Buatlah fungsi untuk melihat keterangan lulus atau tidak lulus :
print("----- No 3 -----")
def nilai(nilai):
    if nilai >= 70:
        print("Lulus")
    else:
        print("Gagal")

nilai(80)
nilai(60)

# Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
print("----- No 4 -----")
def bilangan_ganjil(angka):
    for i in range (1, angka + 1, 2):
        print(i, end = '') 

bilangan_ganjil(20)

