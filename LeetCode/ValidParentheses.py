class Solution(object):
    def isValid(self, s):
        if len(s) & 1:
            return False

        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        append = stack.append
        pop = stack.pop

        for ch in s:
            if ch in '({[':
                append(ch)
            else:
                if not stack or pop() != pairs.get(ch):
                    return False

        return not stack


if __name__ == "__main__":
    s = input("Enter parentheses string: ")
    print(Solution().isValid(s))