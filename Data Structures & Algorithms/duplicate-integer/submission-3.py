class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempDict = dict();
        for i in nums:
            if i in tempDict:
                return True
            tempDict[i]=1
        return False



        