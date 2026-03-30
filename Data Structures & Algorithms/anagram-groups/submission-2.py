class Solution:
    def isAnagram(self, str1, str2) -> bool:
        if len(str1) != len(str2):
            return False
        str2List = list(str2)
        for i in str1:
            if i not in str2List:
                return False
            str2List.remove(i)
        return True        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for i in strs:
            temp = [i]
            for j in strs[strs.index(i)+1:]:
                if self.isAnagram(i,j):
                    strs.pop(strs.index(j,strs.index(i)+1))
                    temp.append(j)
            output.append(temp)
        return output
