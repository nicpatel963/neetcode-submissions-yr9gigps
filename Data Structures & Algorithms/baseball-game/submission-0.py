class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0
        for i in operations:
            match i:
                case 'C':
                    result -= stack.pop()
                case 'D':
                    result += (stack[-1]*2)
                    stack.append(stack[-1]*2)
                case '+':
                    temp = stack.pop()
                    tempSum = stack[-1] + temp
                    result += (tempSum)
                    stack.append(temp)
                    stack.append(tempSum)
                case _:
                    stack.append(int(i))
                    result += int(i)
        return result