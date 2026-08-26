import random
options = ['s', 'w', 'g']

def gamewin(c,p):
    if c==p:
        print("Draw")
    elif c =="s":
        if p=='w':
            print("Computer Win")
        else:
            print("Player Win")

    elif c=="w":
        if p=='g':
            print("Computer Win")
        else:
            print("Player Win")

    elif c=="g":
        if p=='s':
            print("Computer Win")
        else:
            print("Player Win")

round=int(input("How many rounds you want to play:"))
n=0
while n<round:
    print("Round",n+1)
    computer =random.choice(options)
    player=input("Snack(s) Water(w) Gun(g) Player's Option:")
    gamewin(computer,player)
    n+=1