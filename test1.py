class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat, hobi, rank, ipk):
        self.nama = nama
        self.alamat = alamat
        self.hobi = hobi
        self.__rank = rank
        self._ipk = ipk
        Mahasiswa.jumlah_mahasiswa += 1

    def belajar(self):
        print(f"{self.nama} lagi belajar")


m1 = Mahasiswa('dani', 'mataram', 'memancing', 10, 3.4)
m2 = Mahasiswa('dudu', 'jakarta', 'coding', 80, 3.8)
print(Mahasiswa.jumlah_mahasiswa)

m1.belajar()
m2.belajar()
