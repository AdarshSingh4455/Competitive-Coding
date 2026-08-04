# Modify Linear Search to return the position (starting from 1) instead of the index.

n = int(input("Enter the number of element you want in the list: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Enter element {i+1} : ")))

target = int(input("Enter the element you want to search in the list: "))

def searchLinear(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i + 1
    return -1

result = searchLinear(nums, target)

if result == -1:
    print("Not found")
else:
    print(f"{target} found at position: {result}")

# Without using count(), count how many times 10 appears in:

ctarget = int(input("Enter the number to count occurance of that: "))

def searchCountOccurance(nums, ctarget):
    count = 0
    for i in range(len(nums)):
        if nums[i] == ctarget:
            count += 1
    return count

countresult = searchCountOccurance(nums,ctarget)

if countresult == 0:
    print("Element Not found in the list")
else:
    print(f"{ctarget} Element occured {countresult} time in the list.")


# Search the character 'o' in:

text = input("Enter a word: ")
ch = input(f"Enter the char you want to search in this {text} word: ")

def searchCharacter(text, ch):
    for i in range(len(text)):
        if text[i] == ch:
            return i + 1
    return -1

ans = searchCharacter(text,ch)
if ans == -1:
    print("Character Not found.")
else:
    print(f"Entered char {ch} found at {ans} position.")