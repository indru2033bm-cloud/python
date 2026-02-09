d = {} #empty dictionary
marks = {
    "Indrajith":100,
    "Naga":99,
    "sunil":94
}

# print(marks.items()) #returns a list of tuples
# print(marks.keys()) #returns a list of keys
# print(marks.values()) #returns a list of values
# marks.update({"Indrajith":99, "Ramashekar":98 }) #update the value of a key and add a new key-value pair
# print(marks)
print(marks.get("Indrajith2")) #returns the value of the key but does not raise an error if the key is not found, instead returns None
print(marks["Indrajith2"]) #returns the value of the key but raises an error if the key is not found