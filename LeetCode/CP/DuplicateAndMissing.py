"""Title: Duplicate and Missing Number Finder

Description:
This program identifies duplicate values and missing numbers in a given array
containing numbers from 1 to n. It uses a set to track seen elements, prints
any duplicates found, and prints the missing numbers in the range 1..n.
"""

arr = [1, 2, 3, 2, 4]
n = 5
seen = set()

for x in arr:
    if x in seen:
        print(f"Duplicate: {x}")
    else:
        seen.add(x)

for i in range(1, n + 1):
    if i not in seen:
        print(f"Missing: {i}")

print(f"Set: {seen}")