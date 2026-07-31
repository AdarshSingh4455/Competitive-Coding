n=5

for i in range(n+1):
    for k in range(n,i,-1):
        print(" ", end="")

    for j in range(1,i+1):
        print(i, end="")

    for k in range(i-1,0,-1):
        print(i, end="")

    print()