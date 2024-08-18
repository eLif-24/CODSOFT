n=int(input("Enter the no"))
i=n
print(n)
rev=0
while i>0:
    rem=i%10
    rev=rev*10+rem
    print(n)
    i//=10
if rev==n:
    print("The no is palindrome")
else:
    print("The no is not palindrome")

