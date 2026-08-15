nums = [12,18,18,18,30,40]

target = 18

def binarySearch(nums,target):
    answer = -1
    n = len(nums)
    high = n-1
    low = 0

    while low<=high:
        mid = (low + high)//2

        if nums[mid] == target:
            answer = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return answer

x = binarySearch(nums,target)
print(x)