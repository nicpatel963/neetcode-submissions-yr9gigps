class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        for i in s1:
            s1Freq[i] = s1Freq.get(i,0) + 1
        k = len(s1)
        s2Freq = {}
        l = 0
        
        for i in range(len(s2)):
            s2Freq[s2[i]] = s2Freq.get(s2[i], 0) + 1
            while sum(s2Freq.values()) > k:
                if s2Freq[s2[l]] > 1:
                    s2Freq[s2[l]] = s2Freq[s2[l]] - 1
                else:
                    s2Freq.pop(s2[l])
                l += 1
            print(s2Freq)
            if s1Freq == s2Freq:
                return True
            
        return False
