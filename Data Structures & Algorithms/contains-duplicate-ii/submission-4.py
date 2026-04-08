class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}
        for i in range(len(nums)):
            if nums[i] in temp and i - temp[nums[i]] <= k:
                return True
            temp[nums[i]] = i
        return False 