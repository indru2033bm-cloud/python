l = [1,4,9,10]
""""
sqList = []
for i in l:
    sqList.append(i**2)
print(sqList)

"""
sqList = [i**2 for i in l] # This is called list comprehension. It is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expression can be anything, meaning you can put in all kinds of objects in lists.
print(sqList)