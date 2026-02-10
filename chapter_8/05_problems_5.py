# def star(n):
#     for i in range(1,n+1):
#         print("*"*(n+1-i))


def pattran(n):
    if( n == 0):
        return
    print("*" * n)
    pattran(n-1)


n = int(input("Enter a number: "))
# star(n)
pattran(n)