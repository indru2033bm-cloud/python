a = int(input("Enter a your age: "))

if a>=18:
    print("Your are eligible to vote")
    print("Good thing")
elif a == 0:
    print("Your are entered 0 which is not a valid age")
elif a < 0:
    print("Your are entered a negative number which is not a valid age")        
else:
    print("Your not eligibale to vote")  

print("This is the end of the program")