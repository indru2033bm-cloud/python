

with open("poem.txt") as p:
    for poem in p:
        if poem == "TWINKLE":
            print(p.read())