class induk:
    def cobaOverride(self):
        print("ini adalah methode override di kelas induk")


class turunan:
    def cobaOverride(self):
        print("ini adalah methode override di kelas turunan")


# deklasrasi objek kelas induk
objekinduk = induk()
objekinduk.cobaOverride()

# deklarasi objek kelas turunan
objekturunan = turunan()
objekturunan.cobaOverride()
