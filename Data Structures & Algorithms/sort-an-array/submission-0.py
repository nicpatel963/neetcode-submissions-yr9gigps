class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums

        middle = len(nums) //2
        left = nums[:middle]
        right = nums[middle:]

        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)

        return self.merge(left_sorted,right_sorted)
    
    def merge(self,left,right):
        result = []
        i = j = 0

        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])

        return result
