class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(length):
            val = abs(nums[i])
            if 1 <= val <= length:
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] ==0:
                    nums[val-1] = -1 * (length + 1)
        for i in range(1,length+1):
            if nums[i-1] >= 0:
                return i
        return length + 1