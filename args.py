# *args magic keyword parameter tuple
def panggil(*nama):
    print("daftar nama")
    for orang in nama:
        print(orang)

panggil("saitama, goku , naruto ")
print("===" * 10)

# **kwargs magic keyword parameter dictionary
def kirim_sms(*nomor):
    print(nomor)

def tulis_sms(**isi):
    print(isi)


kirim_sms(112, 222, 343)
tulis_sms(tujuan=112, pesan="brembe kabar")
