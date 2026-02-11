import random 

computer = random.choice([1 ,-1 , 0])
def game(com,you):
    if computer == you:
       print("Its draw!")
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

a = 0
while( a != 0):
    youst = input("Enter your choice: ")

    youdic = {"r" : -1,"p" : 0,"c" : 1}

    you = youdic[youst]

    revdic = {-1 : "rock",0 : "paper",1 : "ceaser"}
    print(f"Your choic in {revdic[you]}\nComputer cholic is {revdic[computer]}")



    a =   game(computer,you)
    if a == 1:
       print("YOU Win!")
    with open("Hi-score.txt","w") as f:
        f.write(str(a))
else :
    print("you lose!")




    