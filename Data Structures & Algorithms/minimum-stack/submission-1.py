class MinStack:

    def __init__(self):
        self.stack = []                
        self.index = 0
        self.minVal = 0

    def push(self, val: int) -> None:
        self.stack.append(val)        
        self.index += 1

    def pop(self) -> None:
        self.stack.pop()
        self.index -= 1

    def top(self) -> int:
        return self.stack[self.index-1]

    def getMin(self) -> int:
        if self.index == 0:
            return None
        temp = self.stack.copy()
        minVal = temp.pop()
        index = self.index - 1
        while index != 0:
            popVal = temp.pop()
            minVal = popVal if popVal < minVal else minVal
            index -= 1
        return minVal             

        
