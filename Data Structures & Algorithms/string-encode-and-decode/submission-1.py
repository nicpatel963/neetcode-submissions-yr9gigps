class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result = "".join([result, str(len(i)), '@', i])
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            sub_len = int(s[i:j])
            result.append(s[ j + 1: j + 1 + sub_len])
            i = j + 1 + sub_len
        return result