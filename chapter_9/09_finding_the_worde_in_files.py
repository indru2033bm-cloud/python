with open("log.txt") as f:
    lines = f.readline()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"The word is present in line no {lineno}")
        break
    lineno += 1
else:
    print("The worde is not present ")