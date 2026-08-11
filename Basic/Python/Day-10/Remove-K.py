# Remove K digits from a number sequence to form the smallest possible result
nums = [1,2,4,9,7]
k = 3

def remove_k_elements(nums,k):
    stack = []
    for digit in nums:
        while stack and k>0 and stack[-1]>digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    while k>0 and stack:
        stack.pop()
        k -= 1

    return ''.join(map(str, stack))

res = remove_k_elements(nums,k)
print(res)