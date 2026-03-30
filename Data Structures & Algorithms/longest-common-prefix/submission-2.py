class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = list(strs[0])
        for i in strs:
            if len(i) == 0:
                return ""
            for n in range(len(list(i))):
                if len(result) -1 < n or result[n] != i[n]:
                    result = result[:n]
                    break
                if n == len(i)-1:
                    result = list(i)
        return "".join(result)
