class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack.pop(0)  # ❌ Wrong index — should pop from end

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Expected 3
