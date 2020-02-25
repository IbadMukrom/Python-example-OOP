class Pekerja():
    Jumlah_pekerja= 0
    
    def __init__(self, nama, gaji):
        self.nama = nama 
        self.gaji = gaji
        Pekerja.Jumlah_pekerja += 1

    def tampilkan_jumlah(self):
        print(f"total pekerja {Pekerja.Jumlah_pekerja}")

    def tampilkan_pekerja (self):
        print (f"nama : {self.nama}| gaji {self.gaji}")
 
pekerja1= Pekerja("dani", 200000) # membuat objek pertama dari class pekerja
pekerja2 = Pekerja('danu',40000) #membut objek kedua dari class pekerja
pekerja3 = Pekerja('lala',60000)
pekerja1.tampilkan_pekerja()
pekerja2.tampilkan_pekerja()
print (f"total pekerja : {Pekerja.Jumlah_pekerja}")



    
