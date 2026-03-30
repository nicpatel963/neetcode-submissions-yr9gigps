class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = {}

        for char in s:
            if char in counter_s:
                counter_s[char] += 1
            else:
                counter_s[char] = 1

        for char in t:
            if char not in counter_s or counter_s[char] == 0:
                return False
            counter_s[char] -= 1
        return True                