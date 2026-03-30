class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left = 0
        total = len(height)
        
        if total < 3:
            return 0
        
        while left < total - 1:
            if height[left] == 0:
                left += 1
                continue
            
            right = left + 1
            max_right_idx = right  
            middle = 0

            while right < total and height[right] < height[left]:
                if height[right] > height[max_right_idx]:
                    max_right_idx = right
                middle += height[right]
                right += 1
            
            if right < total:
                water = height[left] * (right - left - 1) - middle
                result += water
                left = right
            else:
                if max_right_idx > left + 1:
                    middle = sum(height[left + 1 : max_right_idx])
                    water = height[max_right_idx] * (max_right_idx - left - 1) - middle
                    result += water
                left = max_right_idx
        
        return result