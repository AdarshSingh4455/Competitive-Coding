nums = [8, 3, 6, 2, 7]

def Slargest_Number(nums):
    n = len(nums)
    max_key = 0
    sec_max = 0
    for i in range(n):
        if nums[i]>max_key:
            sec_max = max_key
            max_key = nums[i]
        elif nums[i]>sec_max and max_key != nums[i]:
            sec_max = nums[i]
    return sec_max


res = Slargest_Number(nums)
print(f"Second Largest number in the list is : {res}")