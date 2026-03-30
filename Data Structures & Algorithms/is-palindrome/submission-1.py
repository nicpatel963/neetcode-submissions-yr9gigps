class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        half_length = len(s)//2
        for i,j in zip(s[:half_length], s[::-1][:half_length]):
            if i != j:
                return False
        return True
