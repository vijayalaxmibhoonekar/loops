n=int(input("enter no:"))
rev=0
while n!=0:
    r=n%10
    n=n//10
    rev=rev*10+r
print("reverse no is:",rev)