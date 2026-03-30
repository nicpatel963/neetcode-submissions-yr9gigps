class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempDict = {}
        for i in nums:
            if i in tempDict:
                return True
            tempDict[i] = i
        
        return False



        