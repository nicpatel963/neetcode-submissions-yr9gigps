class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempDict = dict();
        for i in nums:
            if i in tempDict:
                return True
            tempDict[i]=1
        return False

    def __main():
        s = Solution();
        print(s.hasDuplicate([1,2,3,3]))


        