class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sList = list(s)
        
        for i in list(t):
            if i not in sList:
                return False
            sList.remove(i)
        return True