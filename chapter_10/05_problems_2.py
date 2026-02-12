class calcuater:
    def __init__(self,n):
        self.n = n
    def squre(self):
        print(f"Squre is {self.n ** 2}")
    def cube(self):
        print(f"cube is {self.n ** 3}")
    def squre_root(self):
        print(f"Squre root is {self.n ** 0.5}")
        
a = calcuater(45)      
a.squre()
a.cube()
a.squre_root()