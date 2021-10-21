print('enter your number:')

z=input()
x=len(z)
sum=0
n_int=int(z)

for i in range(x) :
    num=int(z[i])
    sum=num**x+sum

if sum==n_int:
    print("YEEES")
else:
    print("NO")