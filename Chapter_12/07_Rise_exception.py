a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b == 0:
    raise ZeroDivisionError("Cannot divide by Zero")
else:
    print(a/b)
