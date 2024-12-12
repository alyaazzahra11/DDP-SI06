class animal:
    nama = ""
    makanan = ""
    hidup = ""
    berkembang_biak = ""

    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak(self):
        print(f'Hewan {self.nama} memakan {self.makanan}, hewan ini juga hidup di {self.hidup} dan berkembang biak dengan cara {self.berkembang_biak}')

a1 = animal("beruang kutub", "ikan", "darat", "melahirkan")
a1.cetak()

a2 = animal ("kelinci", "wortel", "darat", "melahirkan")
a2.cetak()