class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in table:
                return [table[val],i]
            table[nums[i]] = i
            