class Employe:
    compony = "Google"
    def __init__(self):
        print("Employe is created")
    def show(self):
        print(f"Employ works at {self.compony}")     


class coder(Employe):
    language = "C++"
    def __init__(self):
        super().__init__()
        print("coder is created")
    def showlanguage(self):
        print(f"programmer uses {self.language}")



class programmer( coder):
    salary = 1000000
    def __init__(self):
        super().__init__()
        print("programmer is created")
    def showsalary(self):
        print(f"programmer salary is {self.salary}")


# p = Employe()
# print(p.compony)

# p = coder()
# print(p.compony, p.language)

p = programmer()

print(p.compony, p.language, p.salary)
p.show()
p.showlanguage()
p.showsalary()