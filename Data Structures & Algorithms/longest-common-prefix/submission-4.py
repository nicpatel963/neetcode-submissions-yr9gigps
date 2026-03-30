class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for i in range(len(result)):
            for other in strs[1:]:
                if i == len(other) or result[i] != other[i]:
                    return result[:i]
            
        return result