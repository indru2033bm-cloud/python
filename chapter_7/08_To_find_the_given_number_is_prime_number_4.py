a = int(input("Enter a number: "))

if a <= 1:
    print(a, "not a prime number ")


else:
    for i in range(2 , a):
        if a % i == 0:
            print(a," is not prime number ")
            break
    else:
          print(a," is prime number ")

# a = int(input("Enter a number: "))

# if a <= 1:
#     print(a, "is not prime number")
# else:
#     for i in range(2, a):
#         if a % i == 0:
#             print(a, "is not prime number")
#             break
#     else:
#         print(a, "is prime number")

