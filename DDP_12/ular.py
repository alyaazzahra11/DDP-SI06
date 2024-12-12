from animal import *

class ular(animal):
    warna= ""
    beracun = ""

    def __init__(self, nama, makanan,hidup, berkembang_biak, beracun, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.beracun = beracun
        self.warna = warna

    def cetak_ular (self):
        super().cetak()
        print(f'hewan ini {self.beracun} dan berwarna {self.warna}')

kobra = ular ("ular kobra", "daging", "darat dan air", "bertelur", "memiliki racun", "hitam")
kobra.cetak_ular()

piton = ular ("ular piton", "tikus", "darat dan air", "bertelur", "tidak beracun", "bercorak hitam dan coklat")
piton.cetak_ular()