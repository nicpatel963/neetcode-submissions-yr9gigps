class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charFreq = {}
        for char in s:
            if char in charFreq:
                charFreq[char] += 1
            else:
                charFreq[char] = 1
        
        for char in t:
            if char not in charFreq:
                return False
            elif charFreq[char] == 1:
                charFreq.pop(char)
            else:
                charFreq[char] -= 1
        
        if charFreq:
            return False
        else:
            return True
                
