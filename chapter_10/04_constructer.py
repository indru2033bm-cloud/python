class Employ:
    language = "Python\n"
    salary = 100000

    def __init__(self,name,language,salary): #dunder method which is automatically called

        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getinfo(self):
        print(f"THe language is {self.language}The salary is {self.salary}")


    @staticmethod
    def greet():
        print("Good Moring")
    
indru = Employ("Indrajith","Javascript",1000000)
# indru.language = "Java script\n"
# indru.getinfo()
print(indru.language, indru.salary )