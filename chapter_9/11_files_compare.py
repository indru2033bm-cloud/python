with open("file1.txt") as f:
    contant1 = f.read()
with open("file2.txt") as f:
    contant2 = f.read()

if contant1 == contant2:
    print("Yes content in file1 and file2 are equle")
else:
    print("No content in files are different ")