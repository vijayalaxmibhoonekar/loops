pn=0
for x in range(2,11):
    no=int(input("enter number"))
    for y in range(2,no):
        if(no%y)==0:
            break
    else:
        pn+=1
print("no of prime numbers:",pn)
