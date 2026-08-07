nums = [12, 34, 21, 43, 10]

def SortbyInsertion(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

SortbyInsertion(nums)
print(nums)