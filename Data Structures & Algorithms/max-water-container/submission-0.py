class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i,j = 0,len(heights) - 1
        while i < j:
            left = heights[i]
            right = heights[j]
            height = left if left < right else right
            maxArea = height*(j-i) if height*(j-i) > maxArea else maxArea
            if left < right:
                i+=1
            else:
                j-=1
        return maxArea

    