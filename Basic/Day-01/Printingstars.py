n = int(input("Enter a value: "))
for i in range(1, n + 1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")
    
    print()

# for i in range(n - 1, 0, -1): #agr hum i ko 0 se initiate krte toh output me ...2 baar 5 start wali line print hoti..
for i in range(n - 1, 0, -1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")
    print()