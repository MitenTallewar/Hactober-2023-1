class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

# Example usage of the stack:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack elements:")
while not stack.is_empty():
    print(stack.pop())

print("Is the stack empty?", stack.is_empty())
