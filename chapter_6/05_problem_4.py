a = input("enter your name: ")

b = len(a)

if b>10:
    print("Youe name is grater than 10 characters")
elif b == 0:
    print("You have not entered any name")
elif b<10:
    print("Your name is less than 10 characters")
else:
    print("Your name is exactly 10 characters")