n = int(input("enter a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or i == j:
            print("*", end="")
        else:
            print(" ",end="")
    for k in range(2*(n-i)):
        print(" ", end="")

    for l in range(i+1):
        if l==1 or l==i:
            print("*", end="")
        else:
            print(" ",end="")
    print()

 # for below portion of butterfly
for i in range(n,0,-1):
    for j in range(1,i+1):
        if j==1 or i==j:
            print("*",end="")
        else:
            print(" ",end="")

    print()
