pno=0
Nno=0
for x in range(1,11):
    no=int(input("enter number:"))
    if no>=1:
        pno+=1
    else:
        Nno+=1
print("no of positive numbers:",pno)
print("no of negative numbers:",Nno)