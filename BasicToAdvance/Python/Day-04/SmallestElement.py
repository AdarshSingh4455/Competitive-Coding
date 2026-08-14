nums=[11,45,32,21,10]

def findSmallest(nums):
    minIndex = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[minIndex]:
            minIndex = i
    return nums[minIndex]

result = findSmallest(nums)
print(f"The Smallest Element is : {result}")