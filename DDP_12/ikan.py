from animal import *

class ikan(animal):
    sisik = ""
    warna_sisik = ""

    def __init__(self, nama, makanan,hidup, berkembang_biak, sisik, warna_sisik):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.sisik = sisik
        self.warna_sisik = warna_sisik

    def cetak_ikan (self):
        super().cetak()
        print(f'hewan ini {self.sisik} dan berwarna {self.warna_sisik}')

arwana = ikan ("ikan arwana", "cacing", "air", "bertelur", "memiliki sisik", "putih")
arwana.cetak_ikan()

lele = ikan ("ikan lele", "cacing", "air", "bertelur", "tidak memiliki sisik", "hitam")
lele.cetak_ikan()