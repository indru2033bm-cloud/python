from functools import reduce
max = lambda a ,b: a if a > b else b
l = [4,6,10,8,9]


m = reduce(max,l)
print(m)