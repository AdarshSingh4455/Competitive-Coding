nums = [12,15,18,20,30,40]

target = 30

def binarySearch(nums,target):
    n = len(nums)
    high = n-1
    low = 0

    while low<=high:
        mid = (low + high)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

x = binarySearch(nums,target)
print(x)