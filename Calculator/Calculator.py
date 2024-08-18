#Command Line simple airthmetic calculator
#Project for CodSoft Internship
#Naman Kalra

x,y=0,0
def add():
    x,y=int(input("Enter the First number:")),int(input("Enter the Second number:"))
    c=x+y
    print(f"The Summation of the two number is {c}")
    print("\n")

def sub():
    x,y=int(input("Enter the First number:")),int(input("Enter the Second number:"))
    c=x-y
    print(f"The Difference of the two number is {c}")
    print("\n")

def multi():
    x,y=int(input("Enter the First number:")),int(input("Enter the Second number:"))
    c=x*y
    print(f"The Multiplication of the two number is {c}")
    print("\n")
def div():
    x,y=int(input("Enter the First number:")),int(input("Enter the Second number:"))
    c=x/y
    print(f"The Division of the two number is {c}")
    print("\n")
if __name__=="__main__" :
    print("Hii>>\nWelcome to the N.K. Calculator!!")
    print("\n")
    
    while True:
        print("What Airthmetic Operation would you like to try??")
        print("---------------------------------")
        print("1. Addition.")
        print("2. Subtraction.")
        print("3. Multiplication.")
        print("4. Division.")
        print("5. Exit the application.")
        print("\n")
        n=int(input("Please select from 1-4:"))
        
        if n==1:
            add()
        elif n==2:
            sub()
        elif n==3:
            multi()
        elif n==4:
            div()
        elif n==5:
            print("GoodBye. Have a Great Day!!")
            break
        else:
            print("Invalid Input. Please try again")