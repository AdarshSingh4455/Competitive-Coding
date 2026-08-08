nums = [12,31,24,52,43,10]

def mergeSort(nums):

    if len(nums)<=1:
        return nums

    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left,right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

res = mergeSort(nums)
print(res)