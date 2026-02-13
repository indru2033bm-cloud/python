
class Employe:
    company = "Google"
    def show(self):
        print(f"Employ works at {self.company}")

class programmer(Employe):
    language = "C++"
    def showlanguage(self):
        print(f"programmer uses {self.language}")


o = Employe()

print(o.company)