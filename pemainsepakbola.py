from abc import ABC, abstractmethod


# abstrak method
class PemainSepakbola(ABC):
    nama: str = None
    nomer_punggung: str = None
    usia: int = None
    stamina: float = None

    @abstractmethod
    def lari(self):
        pass


class GoalKeeper(PemainSepakbola):
    reflect: int = None

    # override
    def lari(self):
        print(f'{self.nama}sedang berlari')


gk = GoalKeeper()
gk.nama = "Abdul Aziz"
gk.nomer_punggung = "01"
gk.usia = 21
gk.stamina = 2.3
gk.reflect = 9
gk.lari()
print(f'Goal Keeper : {gk.nama} - {gk.usia} Tahun,- stamina : {gk.stamina}, reflek : {gk.reflect}')

ps = PemainSepakbola()
ps.nama = "Fandi"
ps.lari()
print(f'Pemain Sepakbola : {ps.nama}')
