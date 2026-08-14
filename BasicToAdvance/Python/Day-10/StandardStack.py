class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    # It is for raising an exception when we don't want to hide the error...
    # def pop(self):
    # if not self.items:
    #     raise IndexError("Stack is empty")

    # return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items

    def show(self):
        return self.items

stack = Stack() #creating object naming stack..
stack.push(10)
stack.push(20)
stack.push(30)
print(f"Elements in stacks: {stack.show()}")
print(f"{stack.size()} to see the size of stack before deletion, by using size.")
print(f"{stack.peek()} to see the top element before deletion, by using peek.") #it act as peak to see the top end element of stack..
print(f"{stack.pop()} is deleted from the stack.") #pop is used to remove the top end element of stack..and it returns that value..
print(f"{stack.peek()} to see the top element after deletion, by using peek.")
print(f"{stack.size()} to see the size of stack after deletion, by using size.")
print(f"Remaining elements in stacks: {stack.show()}")
print(f"{stack.pop()} is deleted from the stack.")
print(f"{stack.pop()} is deleted from the stack.")
print(f"{stack.is_empty()} to check stack is empty or not after deletion, by using is_empty.")
print(f"Remaining elements in stacks: {stack.show()}")