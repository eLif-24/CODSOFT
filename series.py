#sum of 9+99+999+9999...n
n=int(input("Enter the no of terms"))
b=0
a=0
i=1
while i<=n:
    b=b*10+9
    a=a+b
    i+=1
print(a)
