class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if not self.items:
            return "Stack is empty"
        return self.items[-1]  # ✅ Top element

s = Stack()
s.push(10)
s.push(20)
print(s.peek())
