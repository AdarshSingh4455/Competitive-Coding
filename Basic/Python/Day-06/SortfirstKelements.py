nums = [8,15,7,5,21,12]
k = 3
def SortFirstK(nums,k):
    for i in range(k):
        min_index = i
        for j in range(i+1,k):
            if nums[j]<nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i] , nums[min_index] = nums[min_index], nums[i]

SortFirstK(nums,k)
print(nums)