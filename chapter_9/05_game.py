import random 
import os



def game(com,you):
    if com == you:
        return -1
    elif com == -1 and you == 1:
        # print("You lose!")
        return 0
    elif com == -1 and you == 0:
        # print("You win!")
        return 1
    elif com == 1 and you == 0:
        # print("You win!")
        return 1
    elif com == 1 and you == -1:
        # print("You lose!")
        return 0
    elif com == 0 and you == 1:
        # print("You win!")
        return 1
    elif com == 0 and you == -1:
        # print("You lose!")
        return 0

total_score = 0
a = 1
while( a != 0):
    computer = random.choice([1 ,-1 , 0])
    youst = input("Enter your choice: ")

    youdic = {"r" : -1,"p" : 0,"c" : 1}

    you = youdic[youst]

    revdic = {-1 : "rock",0 : "paper",1 : "ceaser"}
    print(f"Your choic in {revdic[you]}\nComputer cholic is {revdic[computer]}")



    a =   game(computer,you)
    if a == 1:
            print("You win!")
            total_score += 1
            # if os.path.exists("Hiscore.txt"):
            with open("Hiscore.txt") as f:
                hiscore = (f.read())
                if hiscore != "":
                    hiscore = int(hiscore)
                else:
                    hiscore = 0

            if total_score > hiscore:
                with open("Hiscore.txt", "w") as f:
                    f.write(str(total_score))
            else:
                with open("Hiscore.txt", "w") as f:
                 f.write(str(total_score))
    elif a == -1:
            print("Its draw!")
    else:
            print("you lose!")




    