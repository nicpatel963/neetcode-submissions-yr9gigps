class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = temp
            temp *= nums[i]
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= temp
            temp *= nums[i]
        return result

        
#   2, 3, 4, 5
#  prefix = 1
#  result = [1, 1, 1, 1]
#  result[0] = prefix 1
#  prefix *= num[0]  2
#  1, 2, 6, 24
#  24, 30, 40, 60