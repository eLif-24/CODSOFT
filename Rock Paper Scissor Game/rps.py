#Rock Paper Scissors Game
import random

options=[1,2,3]
options_1={1:"Rock",2:"Paper",3:"Scissors"}
def rps_comp():
    z=random.choice(options_1)
    return z
def game(k,y):
    if k==y:
        print("It's a Tie!")
    elif k=='Rock' and y=='Scissors':
        print("You win!")
    elif k=='Paper' and y=='Rock':
        print("You win!")
    elif k=='Scissors' and y=='Paper':
        print("You win!")
    else:
        print("You Lose")
    
    
    
print("Welcome to Rock Paper and Scissors!!")
print("------------------------------------")
running=True
while running:  
    x=None
    
    while x not in options:
        print("What would you like to choose?")
        print("1.Rock\n2.Paper\n3.Scissors\n")
        x=int(input("Please enter the choice number:\n"))
    k=options_1[x]
    y=rps_comp()
    print(f"You choose: {k}")
    print(f"Computer choose: {y}")
    game(k,y)
    if not input("Do you want to play again: (Y/N)").upper()=="Y":
        running=False
print("Thanks for playing!!")

    
    