a = int(input("Enter a number: "))

fact = 1
if a == 1:
    print("Factoral =",a)
else:
    for i in range(2,a+1 ):
       fact *= i

print("Factoral = ",fact)
