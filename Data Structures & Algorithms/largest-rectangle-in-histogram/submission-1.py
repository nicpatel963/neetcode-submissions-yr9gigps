class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [] # Stores [height, index]
        # Add a 0 at the end to force the stack to clear out at the finish line
        heights.append(0)
        for i in range(len(heights)):
            # While the current bar is shorter than the one on the stack
            while stack and stack[-1][0] > heights[i]:
                height, index = stack.pop()
                # If stack is empty, it means the popped height was the 
                # smallest seen so far; it can span the entire width 'i'
                if not stack:
                    width = i
                else:
                    # Width is current index 'i' minus index of new top element - 1
                    width = i - stack[-1][1] - 1
                ans = max(ans, height * width)
            stack.append([heights[i], i])
        return ans