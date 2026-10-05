class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low = max(low - 1, 0)
                high -= 1
            else:  # ch == '*'
                low = max(low - 1, 0)
                high += 1

            if high < 0:
                return False

        return low == 0


# Example usage:
# sol = Solution()
# print(sol.checkValidString("()"))      # True
# print(sol.checkValidString("(*)"))     # True
# print(sol.checkValidString("(*))"))    # True
# print(sol.checkValidString("("))       # False
