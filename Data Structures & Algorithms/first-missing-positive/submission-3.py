class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != i+1:
                index = nums[i]-1
                if nums[index] != nums[i]:
                    print(nums[i],index,nums[index])
                    nums[index],nums[i] = nums[i],nums[index]
                    print(nums)
                    i-=1
            i+=1

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        
        return len(nums)+1


