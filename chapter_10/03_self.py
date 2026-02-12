class Employ:
    language = "Python\n"
    salary = 100000


    def getinfo(self):
        print(f"THe language is {self.language} \nThe salary is {self.salary}")


    @staticmethod
    def greet():
        print("Good Moring")
    
indru = Employ()
# indru.language = "Java script\n"
indru.getinfo()
# print(indru.language, indru.salary )