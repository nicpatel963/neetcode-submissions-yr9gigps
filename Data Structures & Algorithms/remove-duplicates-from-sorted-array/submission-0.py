class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        n = 0 
        while n < len(nums):
            nums[k] = nums[n]
            while n < len(nums) and nums[n] == nums[k]:
                n+=1
            k+=1
        return k