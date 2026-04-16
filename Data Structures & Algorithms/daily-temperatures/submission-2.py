class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for temp in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[temp]:
                n = stack.pop()
                result[n] = temp - n
            stack.append(temp)
        return result
