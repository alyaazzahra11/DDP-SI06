import math

def persegi (sisi):
    hasil = sisi ** 2
    print("Luas Persegi dengan sisi", sisi, "cm", "adalah", hasil, "cm^2")

def segitiga (alas, tinggi):
    hasil = 1/2 * alas * tinggi
    print("Luas Segitiga dengan alas", alas, "cm dan tinggi", tinggi, "cm adalah", hasil, "cm^2")

def persegi_panjang (panjang, lebar):
    hasil = panjang * lebar
    print("Luas Persegi panjang dengan panjang", panjang, "cm dan lebar", lebar, "cm adalah", hasil, "cm^2")

def jajar_genjang (alas, tinggi):
    hasil = alas * tinggi
    print("Luas Jajar genjang dengan alas", alas, "cm dan tinggi", tinggi, "cm adalah", hasil, "cm^2")

def layang_layang (d1, d2):
    hasil = 1/2 * d1 * d2
    print("Luas Layang-layang dengan diagonal", d1, "cm dan", d2, "cm adalah", hasil, "cm^2")