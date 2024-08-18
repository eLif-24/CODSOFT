import math
n=int(input("Enter the no"))
i=n
c=0
while i>0:
    c+=1
    i//=10
i=n
a=0
while i>0:
    rem=i%10
    a=a+pow(rem,c)
    i//=10
if a==n:
    print("The no is armstrong")
else:
    print("The no is not armstrong")