try:
    a = int(input("Hey there, enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("Hi there,I am in else block ") # This block will only execute if there is no exception in try block or if there is an exception but it is handled in except block.