class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            if len(stack) == 0:
                stack.append([temperatures[i],i])
                continue
            print(stack)
            while len(stack) != 0 and stack[-1][0] < temperatures[i]:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i],i])
        return ans