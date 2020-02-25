class father:
    def methodfather(self):
        print("this is method father")

class child (father):
    def methodchild (self):
        print("this is methode child")

# deklarasi objek father
a = father()
a.methodfather()

# deklarasi method child
b = child ()
b.methodchild ()
b.methodfather ()