class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		write = 0
		for num in nums:
			if num != val:
				nums[write] = num
				write += 1
		return write
