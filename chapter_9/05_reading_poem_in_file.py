

with open("poem.txt") as p:
    for poem in p:
        if poem.startswith("TWINKLE"):
           print("Poem as TWINKLE")
           print("\n")
           print(p.read())  
           print("\n")  

