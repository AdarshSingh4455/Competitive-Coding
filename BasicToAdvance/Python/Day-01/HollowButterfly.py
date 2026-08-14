n = int(input("enter a number: "))

# upper half
for i in range(1, n+1):
    # left wing
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")

    # middle spaces
    for _ in range(2 * (n - i)):
        print(" ", end="")

    # right wing
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# lower half
for i in range(n, 0, -1):
    # left wing
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")

    # middle spaces
    for _ in range(2 * (n - i)):
        print(" ", end="")

    # right wing
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
