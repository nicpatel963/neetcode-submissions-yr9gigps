class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        heights.append(0)
        for i in range(len(heights)):
            while stack and stack[-1][0] > heights[i]:
                height,index = stack.pop()
                
                if not stack:
                    width = i
                else:
                    width = i - stack[-1][1] - 1
                
                ans = max(ans, height * width)
            stack.append([heights[i],i])
        return ans
                    