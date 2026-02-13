class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"TwoD vector = {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"ThreeD vector = {self.i}i + {self.j}j + {self.k}k")


a = TwoDvector(2,5)
a.show()

b = ThreeDvector(2,4,6)
b.show()