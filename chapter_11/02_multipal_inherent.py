class Employe:
    compony = "Google"
    def show(self):
        print(f"Employ works at {self.compony}")        
class coder:
    language = "C++"
    def showlanguage(self):
        print(f"programmer uses {self.language}")
class programmer(Employe, coder):
    salary = 1000000
    def showsalary(self):
        print(f"programmer salary is {self.salary}")

p = programmer()

print(p.compony, p.language, p.salary)
p.show()
p.showlanguage()
p.showsalary()