class Employe:

    def __init__(self,n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
    
a = Employe(2)
b = Employe(3)

print(a + b)