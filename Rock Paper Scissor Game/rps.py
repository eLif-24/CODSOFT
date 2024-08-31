#Rock Paper Scissors Game
import random

comp=0
user=0

z=int()
def rps_comp():
    y=[1,2,3]
    z=random.choice(y)
    return z
def game(x,y,comp,user):
    comp,user=0,0
    if x==1 and y==1:
        print("This is a tie\n")
    elif x==1 and y==2:
        print("Comp wins\n")
        comp=+1
    elif x==1 and y==3:
        print("You win\n")
        user=+1
    elif x==2 and y==1:
        print("You win\n")
        user=+1
    elif x==2 and y==2:
        print("This is a tie\n")
    elif x==2 and y==3:
        print("Comp wins\n")
        comp=+1
    elif x==3 and y==1:
        print("Comp wins\n")
        comp=+1
    elif x==3 and y==2:
        print("You win\n")
        user=+1
    elif x==3 and y==3:
        print("This is a tie\n")
    else:
        print("Invalid choice")
    

    
    
print("Welcome to Rock Paper and Scissors!!")
print("------------------------------------")


while True:
    print("What would you like to choose?")
    print("1.Rock\n2.Paper\n3.Scissors\n4.exit")
    
    x=int(input("Please enter the choice:\n"))
    y=rps_comp()
    if x==1:
        print("You choose Rock")
    elif x==2:
        print("You choose Paper")
    elif x==3:
        print("You choose scissors")
    if x==1 or x==2 or x==3:
        if y==1:
            print("Computer choose Rock\n")
        elif y==2:
            print("Computer choose Paper\n")
        elif y==3:
            print("Computer choose scissors\n")
    if x!=4:
        game(x,y,comp,user)
    elif x==4:
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice\n")
        break