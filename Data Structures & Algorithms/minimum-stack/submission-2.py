class MinStack:

    def __init__(self):
        self.smallest = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            if val < self.smallest[-1]:
                self.smallest.append(val)
            else:
                self.smallest.append(self.smallest[-1])
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.smallest.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.smallest.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1]
