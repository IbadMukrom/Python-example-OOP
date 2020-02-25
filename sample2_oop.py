from abc import ABC, abstractmethod

#abstract class
class PemainSepakbola(ABC):
    nama:str = None
    nomer_punggung:str = None
    usia:int = None
    stamina:float = None

    @abstractmethod
    def lari(self):
        pass
        

class GoalKeeper(PemainSepakbola):
    reflect:int = None

    #override method
    def lari(self):
        print(f'{self.nama} sedang berlari')


class Back(PemainSepakbola):
    body_balance:int = 0

    #override method
    def lari(self):
        print(f'{self.nama} sedang berlari')




gk = GoalKeeper()
gk.nama = "Abdul Aziz"
gk.nomer_punggung = "01"
gk.usia = 21
gk.stamina = 2.3
gk.reflect = 9
gk.lari()

print(f'Goal Keeper : {gk.nama} - Usia {gk.usia} Tahun | Stamina {gk.stamina} | Reflect {gk.reflect}')

b1 = Back()
b1.nama = "Ibad"
b1.body_balance = 9
b1.usia = 23
b1.stamina = 6.0
b1.lari()

# ls = [gk, b1]

print(f"Back :{b1.nama}- Usia {b1.usia} Tahun | body balance {b1.body_balance} | Stamina {b1.stamina}")

# ls[0].lari()
# ls[1].lari()   
# for l in ls:
    # l.lari()
    