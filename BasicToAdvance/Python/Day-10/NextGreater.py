arr = [12,10,14,7,15]

def next_greater_element(arr):
    result = [-1]*len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):

        current = arr[i]
        while stack and stack[-1]<=current:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(current)
    return result

res = next_greater_element(arr)
print(arr)
print(res)