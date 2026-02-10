import random

computer = random.choice([-1 , 0 , 1])
yourstr = input("Enter your choice : ")
yourdic  = {
    "r" : -1,
    "p" : 0 ,
    "c" : 1
}
reverseddic = {
    -1 : "Rock",
    0 : "Paper",
    1 : "Caesar"
}

you = yourdic[yourstr]

print(f"you selected {reverseddic[you]} \nComputer selected {reverseddic[computer]}")

if computer == you:
    print("Its is draw")
else:
    if computer == -1 and you == 0:
        print("You win")
    elif computer == -1 and you == 1:
        print("You lose!")
    elif computer == 0 and you == 1:
        print("You win")
    elif computer == 0 and you == -1:
        print("You win")
    elif computer == 1 and you == 0:
        print("You win")
    elif computer == 1 and you == -1:
        print("You win")
    else:
        print("Somthing went wrong ")
 