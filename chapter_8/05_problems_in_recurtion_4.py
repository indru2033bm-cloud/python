# def sum(n):
#     sum = 0
#     for i in  range(1,n+1):
#         sum += i
#     return sum

def sum(n):
    if n == 1:
        return 1
    return sum(n - 1) + n


n = int(input("Enter a number: "))

print("Sum of N natural number ",sum(n))