#map Example
l = [1,2,3,4,5]
squre = lambda n: n * n

sq = map(squre,l)
print(list(sq))

#filter Example
def even(n):
    if n % 2 == 0:
        return True
    return False

Even_no_list = filter(even,l)
print(list(Even_no_list))

#reduce Example
from functools import reduce
add = lambda x,y: x*y

mul = reduce(add,l)
print(mul)