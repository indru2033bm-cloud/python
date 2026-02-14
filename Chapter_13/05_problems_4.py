def fix(n):
    if n % 5 == 0:
        return True
    return False

l = [1,2,3,4,5,6,7,8,9,10]
new_list = filter(fix,l)
print(list(new_list))