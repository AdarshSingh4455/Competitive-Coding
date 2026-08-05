# Make the list Sorted in Ascending Order..
nums = [15,7,12,9,13]

def bubbleSort(nums):
    n = len(nums)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped = True
        if not swapped:
            break

bubbleSort(nums)
print(nums)

# Make the list Sorted in Descending Order..
def bubbleSortDesc(nums):
    n = len(nums)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if nums[j]<nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped = True
        if not swapped:
            break

bubbleSortDesc(nums)
print(nums)