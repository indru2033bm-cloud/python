

with open("log.txt") as f:
    contane = f.read()

if "python" in contane:
      print("The word is present in the file")
else:
     print("The word python is not present")
