stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(f"Elements in stacks: {stack}")
print(f"{stack[-1]} to see the top element before deletion by using peek.") #it act as peak to see the top end element of stack..
print(f"{stack.pop()} is deleted from the stack.") #pop is used to remove the top end element of stack..and it returns that value..
print(f"{stack[-1]} to see the top element after deletion by using peek.")
print(f"Remaining elements in stacks: {stack}")