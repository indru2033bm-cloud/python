import random

def game():
    print("You are playing game ...")
    score = random.randint(1,132)
    print(f"score {score}")

    #Feating the data from file

    with open("Hi-score.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
    if score > hiscore:
        # writing the updataed score
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    return score

game()
        
