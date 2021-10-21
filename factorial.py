import math

n=int(input("please enter number: "))
for i in range(n):

    if math.factorial(i)==n:
        print("YES")
        exit()

print("NO")