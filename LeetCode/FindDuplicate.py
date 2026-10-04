"""Find the duplicate number using Floyd's cycle detection algorithm."""

nums = [2, 4, 3, 1, 2]

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Phase 1
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # Phase 2
    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

ans = findDuplicate(nums)
print(ans)