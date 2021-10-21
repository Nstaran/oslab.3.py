import random

n=int(input("Eplease nter the size of array: "))
array=[]
for i in range(n):
    while(True):
        rand1=random.randint(0,120)
        if rand1 not in array:
            break
    array.append(rand1)
print(array) 