class Integer:
    def __init__(self, val):
        self.val = val
    
    def __repr__(self):
        return str(self.val)
    
    def __call__(self):
        return self.val
    
    def __add__(self, other):
        return self.val + other.val
    
    def __sub__(self, other):
        return self.val - other.val
    
    def __mul__(self, other):
        return self.val * other.val
        

i1 = Integer(10)
i2 = Integer(50)
print(i1+i2)
print(i1-i2)
print(i1*i2)
