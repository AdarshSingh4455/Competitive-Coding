nums = [12, 34, 23, 54, 11, 10]

def secondSmallest(nums):
    n = len(nums)
    if n < 2:
        return None

    for i in range(2):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums[1]

res = secondSmallest(nums)
print(f"The second smallest element is : {res}")