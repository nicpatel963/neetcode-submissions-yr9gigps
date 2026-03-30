class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for index,value in enumerate(nums):
            if target-value in numDict:
                return [numDict[target-value],index]
            numDict[value] = index
