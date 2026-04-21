class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = {}
        res = 0
        l = 0
        
        for r in range(len(s)):
            # 1. Add right character to state
            charSet[s[r]] = 1 + charSet.get(s[r], 0)
            
            # 2. Check if window is invalid
            # Total Window Size (r - l + 1) minus the count of the most frequent char
            # tells us how many replacements are needed.
            while (r - l + 1) - max(charSet.values()) > k:
                # Shrink from the left
                charSet[s[l]] -= 1
                l += 1
            
            # 3. Update the result
            res = max(res, r - l + 1)
            
        return res