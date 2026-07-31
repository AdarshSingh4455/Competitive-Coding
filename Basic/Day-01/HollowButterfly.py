n = int(input("enter a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or i == j:
            print(j, end="")
        else:
            print(" ",end="")
    for k in range(2*(n-i)):
        print(" ", end="")

    for l in range(i+1):
        if l==1 or l==i:
            print(l, end="")
        else:
            print(" ",end="")
    print()

 # for below portion of butterfly
for i in range(n,0,-1):
    for j in range(1,i+1):
        if j==1 or i==j:
            print(j,end="")
        else:
            print(" ",end="")
    for k in range(2*(n-i),0,-1):
        print("_", end="")

    for j in range(n,0,-1):
        if j ==1 or j==i:
            print(j, end="")
        else:
            print(" ", end="")

    print()
