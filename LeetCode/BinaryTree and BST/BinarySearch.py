#Problem number 704 on leetcode

class Solution(object):
    def __init__(self, nums=None, target=None):
        self.nums = nums if nums is not None else []
        self.target = target

    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    solution = Solution(nums, target)
    print(solution.search(solution.nums, solution.target))

