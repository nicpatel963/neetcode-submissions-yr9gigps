class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp = []
        minval = self.stack[-1]
        while self.stack:
            val = self.stack.pop()
            if val < minval:
                minval = val
            temp.append(val)

        while temp:
            self.stack.append(temp.pop())
        return minval