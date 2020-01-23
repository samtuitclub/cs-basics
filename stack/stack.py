class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return true
        return false

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return 0
        return self.stack[len(self.stack)-1]

