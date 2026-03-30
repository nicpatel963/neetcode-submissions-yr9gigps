class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        hasZero = False
        for i in nums:
            if i:
                total = total*i
            elif hasZero:
                total = 0
            else:
                hasZero = True
        result = []
        for i in nums:
            if i == 0 and hasZero:
                result.append(total)
            elif hasZero:
                result.append(0)
            else:
                result.append(total//i)
        return result