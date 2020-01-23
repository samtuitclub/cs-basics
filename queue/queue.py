class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return true
        return false

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        return self.queue.pop()

    def length(self):
        return len(self.queue)

    def head(self):
        if self.length() == 0:
            return 0
        return self.queue[self.length()-1]

    def tail(self):
        return self.queue[0]


