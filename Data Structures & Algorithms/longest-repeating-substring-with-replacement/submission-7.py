class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            charSet[s[r]] = 1 + charSet.get(s[r],0)
            maxf = max(charSet[s[r]],maxf)
            while (r-l+1 - maxf) > k:
                charSet[s[l]] -= 1
                l+=1

            res = max(res, r-l+1)
        return res