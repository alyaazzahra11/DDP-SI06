class Gempa:
    lokasi = " "
    skala = " "

    # kontraktor instalasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # method penentu dampak gempa
    def dampak (self):
        # statement
        if self.skala < 2:
            print("Gempa tidak berasa")
        elif 2 >= self.skala <= 4:
            print("Gempa berdampak bangunan retak-retak")
        elif 4 >= self.skala <=6:
            print("Gempa berdampak bangunan roboh")
        elif 6 > self.skala:
            print("Gempa berdampak bangunan roboh dan berpotensi tsunami")
        else:
            print("")

            # menampilkan hasil
        print(f"Lokasi Gempa: {self.lokasi}")
        print(f"Skala Gempa: {self.skala}")