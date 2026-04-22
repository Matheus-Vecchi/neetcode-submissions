class MinStack:

    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.aux) == 0:
            self.aux.append(val)
        else:
            if val < self.aux[-1]:
                self.aux.append(val)
            else:
                self.aux.append(self.aux[-1])

    def pop(self) -> None:
        self.aux.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.aux[-1]
