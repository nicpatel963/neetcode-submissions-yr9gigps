class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tFreq,window = {},{}
        for i in t:
            tFreq[i] = tFreq.get(i,0) + 1

        have,need = 0,len(tFreq)
        l = 0
        res,resLen = [-1,-1], len(s) + 1
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in tFreq and window[c] == tFreq[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in tFreq and window[s[l]] < tFreq[s[l]]:
                    have -= 1
                l+= 1
        l,r = res
        return s[l:r+1] if resLen != len(s) + 1 else ""