class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Freq = {}
        s2Freq = {}
        for i in range(len(s1)):
            s1Freq[s1[i]] = s1Freq.get(s1[i], 0) + 1
            s2Freq[s2[i]] = s2Freq.get(s2[i], 0) + 1
            
        if s1Freq == s2Freq: return True
        
        # Fixed window sliding
        for i in range(len(s1), len(s2)):
            # Add new character
            char_in = s2[i]
            s2Freq[char_in] = s2Freq.get(char_in, 0) + 1
            
            # Remove old character
            char_out = s2[i - len(s1)]
            if s2Freq[char_out] == 1:
                del s2Freq[char_out]
            else:
                s2Freq[char_out] -= 1
                
            if s1Freq == s2Freq:
                return True
                
        return False