class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums)):
            if count >= len(nums)/2:
                return nums[i-1]
            if nums[i] == nums[i-1]:
                count +=1
            else:
                count = 1 
        return nums[-1]
