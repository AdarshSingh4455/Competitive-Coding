nums = [2, 4, 6, 8]
x = int(input(f"Enter a element you want to insert in this list : {nums} "))

def insert_Element(nums,x):
    n = len(nums)
    nums.append(0)
    j = n - 1
    while j >= 0 and nums[j] > x:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = x

insert_Element(nums,x)
print(nums)