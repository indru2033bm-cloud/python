
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# try:
#     if b == 0:
#         raise ZeroDivisionError("Cannot divide by Zero")
#     else:
#         print(a/b)

if b == 0:
    raise ZeroDivisionError("It Gives infinity")
else:
    print(a/b)