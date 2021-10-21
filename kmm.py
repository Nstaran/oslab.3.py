a=int(input("enter first number:"))
b=int(input("enter secend number:"))
if a>b:
    s=b
else:
    s=a
s+=1
for i in range(1,s):
    if((a%i==0)and(b%i==0)):
        bmm=i
kmm= int((a*b)/bmm)
print(kmm)