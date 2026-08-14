class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))