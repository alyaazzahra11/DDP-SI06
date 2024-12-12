from animal import *

class burung(animal):
    warna = ""
    bentuk_paruh = ""

    def __init__(self, nama, makanan,hidup, berkembang_biak, warna, bentuk_paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.bentuk_paruh = bentuk_paruh

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berwarna {self.warna} dan memiliki bentuk paruh yang {self.bentuk_paruh}')

kakatua = burung ("burung Kakatua", "biji-bijian", "udara", "bertelur", "merah", "bengkok")
kakatua.cetak_burung()

dara = burung ("burung dara", "biji-bijian", "udara", "bertelur", "putih", "bengkok")
kakatua.cetak_burung()