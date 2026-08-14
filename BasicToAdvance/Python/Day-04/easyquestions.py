# Q1: Write a function that returns True if the target exists in the list, otherwise False.
list1 = [20,30,31,43]

def IsinList(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False

print(IsinList(list1,32))

#Q2: Write a function that returns -1 if the list is empty.

def IsListEmpty(nums):
    if len(nums) == 0:
        return -1
    return False


print(IsListEmpty([]))