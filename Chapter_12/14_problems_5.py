n = 5

Tables = [n * i for i in range(1, 11)]
with open("Tables.txt","w") as f:
    for table in Tables:
        f.write(str(table) + "\n")