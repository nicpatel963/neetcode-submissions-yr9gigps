class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left = 0
        total = len(height)
        
        if total < 3:
            return 0
        
        while left < total - 1:
            # Skip zeros on left
            if height[left] == 0:
                left += 1
                continue
            
            right = left + 1
            max_right_idx = right  # Track tallest bar if we don't find one >= left
            middle = 0
            
            # Find right boundary >= left, or track the tallest
            while right < total and height[right] < height[left]:
                if height[right] > height[max_right_idx]:
                    max_right_idx = right
                middle += height[right]
                right += 1
            
            if right < total:
                # Found a wall >= left
                water = height[left] * (right - left - 1) - middle
                result += water
                left = right
            else:
                # Didn't find wall >= left, restart from max_right_idx
                # Calculate water bounded by max_right
                if max_right_idx > left + 1:
                    # Recalculate middle up to max_right_idx
                    middle = sum(height[left + 1 : max_right_idx])
                    water = height[max_right_idx] * (max_right_idx - left - 1) - middle
                    result += water
                left = max_right_idx
        
        return result