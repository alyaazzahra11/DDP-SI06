import math

def kubus (sisi):
    luas = 6 * (sisi * sisi)
    print("Luas permukaan Kubus dengan sisi", sisi, "cm adalah", luas, "cm^2")

def balok (panjang, lebar, tinggi):
    luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    print("Luas permukaan Balok dengan panjang", panjang, "cm, lebar", lebar, "cm dan tinggi", tinggi, "cm adalah", luas, "cm^2")

def kerucut (r, sisi):
    luas = (3.14 * r * sisi) + (3.14 * r * r)
    print("Luas permukaan Kerucut dengan jari-jari", r, "cm dan sisi", sisi, "cm adalah", luas, "cm^2")

def bola (r):
    luas = 4 * 3.14 * (r ** 2)
    print("Luas permukaan Bola dengan jari-jari", r, "cm adalah", luas, "cm^2")

def tabung (tinggi, r):
    luas = 2 * 3.14 * (tinggi + r)
    print("Luas permukaan Tabung dengan tinggi", tinggi, "cm dan jari-jari", r,"cm adalah", luas, "cm^2")

def prisma (tinggi, alas, sisi):
    luas_alas = 1/2 * alas * tinggi
    keliling_alas = sisi * sisi * sisi
    luas = (2 * luas_alas) + (keliling_alas * tinggi)
    print("Luas permukaan prisma dengan luas alas", luas_alas, "cm^2, keliling alas", keliling_alas, "cm dan tinggi", tinggi, "cm adalah", luas, "cm^2")