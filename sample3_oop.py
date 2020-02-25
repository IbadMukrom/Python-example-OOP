class Array:
    def __init__(self, *args):
        self.val = list(args)
        
    def __len__(self):
        return len(self.val)
    
    def __getitem__(self, idx):
        return self.val[idx]
    
    def __repr__(self):
        return str(self.val)


a = Array(1,2,3,4)
print(len(a))
print(a)
print(a[0])
