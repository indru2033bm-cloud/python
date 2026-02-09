a = int(input("Enter a number  1: "))
b = int(input("Enter a number  2: "))
c = int(input("Enter a number  3: "))
d = int(input("Enter a number  4: "))

if a>b and a>c and a>d:
    print(a," is the grater number")
elif b>a and b>c and b>d:
    print(b," is grater number")
elif c>a and c>b and c>d:
    print(c," is grater number")   
else:
    print(d," is grater number")       