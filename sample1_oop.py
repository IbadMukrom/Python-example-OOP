nama_manusia = None
tinggi_manusia = None
berat_manusia = None


# encapsulation or blue print
class Manusia:
    nama: str = None
    tinggi: float = None
    berat: float = None

    def __init__(self, nama: str = None):
        self.nama = nama

    def makan(self):
        print(f'{self.nama} sedang makan')


m1 = Manusia(nama="fandi")
m1.tinggi = 170.5
m1.berat = 65

print(f"Object m1")
print(f"nama \t: {m1.nama}")
print(f"tinggi \t: {m1.tinggi} cm")
print(f"berat \t: {m1.berat} kg")
m1.makan()
print()

m2 = Manusia(nama="Ivan Rialdi")
m2.tinggi = 170
m2.berat = 67
print(f"Object m2")
print(f"nama \t: {m2.nama}")
print(f"tinggi \t: {m2.tinggi} cm")
print(f"berat \t: {m2.berat} kg")
m2.makan()
