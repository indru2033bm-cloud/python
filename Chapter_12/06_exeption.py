try:
    a = int(input("Hey there, enter a number: "))
    print(a)
except ValueError as v:
    # print(v)
    print("Please enter a valid number")

except Exception as e:
    print(e)