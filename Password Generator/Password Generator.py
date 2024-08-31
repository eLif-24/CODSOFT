#Command Line Password Generator
#Project for CodSoft Internship
#Naman Kalra

import random
option="abcdefghijklmnopqrstuvwxyz123456789@_-.$!ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def password(x):
    pass_word=random.choices(option,k=x)
    z=''.join(pass_word)
    return z



print("Hii>>\nWelcome to the Password Generator!!")
print("------------------------------------------\n")
name=input("What is your name?\n")
x=int(input("Enter the length of password: "))
y=password(x)
print(f"Your password is: {y}")