n = int(input("Enter number of elements you want in the list : "))
nums = []
print("Enter the elements of the list :-\n")
for i in range(n):
    nums.append(int(input(f"Enter the element {i+1} : ")))

target =int(input("Enter the number you want to search in the list : "))


def linearSearch(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i

    return -1

result = linearSearch(nums,target)
if result == -1:
    print("Not Found")
else:
    print(f"{target} found at index : {result}\nposition : {result+1}")