class programmer:
    name = "none"
    language = "C++"
    salary = 100000

    def __init__(self,name,language,salary):
            self.name = name
            self.language = language
            self.Salary = salary

programmers = []
n = int(input("Enter number of programmer: "))

for i in range(1,n+1):
    name = input("Enter the name of programmer: \n")
    langu = input("Enter the language : \n")
    salary = (input("Enter the salary: \n"))
    p = programmer(name,langu,salary)
    programmers.append(p)
    # with open("programmer.txt","w") as f:
    #     f.write(f"Name of the programmer is {p.name} \nLanguage is {p.language} \nSalary is {p.salary} \n----------- 00 ----------")

  
  
print("Datels of the programmer are:" )
for i in range(1,n+1):
    print(p.name,p.language,p.Salary)

print(programmers)