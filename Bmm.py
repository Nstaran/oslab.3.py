import math
a=int(input("enter number1:"))
b=int(input("enter number2:"))
if a>b:
    s=b
else:
    s=a
s+=1
for i in range(1,s):
    if((a%i==0)and(b%i==0)):
        bmm=i
print(bmm)