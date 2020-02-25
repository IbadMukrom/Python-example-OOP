
class Karnivora:
    berkaki_empat: str = None
    berdarah_panas: str = None
    vivipar: str = None

    def __init__(self, berkaki_empat:str = None):
        self.berkaki_empat = berkaki_empat

    def makan (self):
        print (f'{self.berkaki_empat} sedang tidur')

k1 = Karnivora(berkaki_empat="serigala")
k1.berdarah_panas = "iya"
k1.vivipar = "iya"


print (f"berkaki_empat \t: {k1.berkaki_empat}")
print (f"berdarah_panas \t:{k1.berdarah_panas}")
print (f"vivipar \t: {k1.vivipar}")
k1.makan()




