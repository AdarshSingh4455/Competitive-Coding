nums = [12, 45, 7, 61, 28]

def largest_Number(nums):
    n = len(nums)
    max_key = nums[0]
    for i in range(1,n):
        if nums[i]>max_key:
            max_key = nums[i]
    return max_key


res = largest_Number(nums)
print(f"Largest number in the list is : {res}")