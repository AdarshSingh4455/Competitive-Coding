nums = [21,34,23,54,65,45]

def SelectionSort(nums):
    n = len(nums)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if nums[j]<nums[minIndex]:
                minIndex = j
        if minIndex != i:
            nums[i],nums[minIndex] = nums[minIndex],nums[i]

SelectionSort(nums)
print(f"List sorted by Selection Sort: {nums}")
