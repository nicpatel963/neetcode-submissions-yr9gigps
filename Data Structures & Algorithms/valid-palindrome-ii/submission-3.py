class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = ''.join( char.lower() for char in s if char.isalnum())
        i,j = 0,len(s)-1
        def is_palindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        
        while i < j:
            if s[i] != s[j]:
                return is_palindrome(i+1,j) or is_palindrome(i,j-1)
            i+=1
            j-=1
        
        return True