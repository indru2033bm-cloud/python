s = {34,12,34,"Indrajith", "Naga", "Indrajith"}

print(s) #sets do not allow duplicate values and do not maintain order
s.add("Ramashekar") #add a new element to the set
# s.clear() #remove all elements from the set
s.discard("Naga") #remove an element from the set if it is present, does not raise an error if the element is not found
# s.remove("Naga") #remove an element from the set if it is present, raises   an error if the element is not found
print(s)                