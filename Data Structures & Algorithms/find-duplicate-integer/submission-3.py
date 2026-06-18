class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = abs(nums[i]) -1
            if nums[temp] < 0:
                return abs(nums[i])
            else:
                nums[temp] *= -1
        return -1