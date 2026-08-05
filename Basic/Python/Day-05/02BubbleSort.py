# Write Bubble Sort for Strings. Sort them in alphabetical order.
arr = ["Hello", "Namaste", "KemChho"]


def SortString():
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break;


SortString()
print(arr)