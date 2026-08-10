class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

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

def balance_brackets(expr):
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = Stack()

    for ch in expr:
        if ch in '({[':
            stack.push(ch)
        elif ch in ')}]':
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()

if __name__ == '__main__':
    print(balance_brackets('({[]})'))
    print(balance_brackets('([)]'))
    print(balance_brackets('(([]))'))
