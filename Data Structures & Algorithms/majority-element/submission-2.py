class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]
        for i in nums:
            if i == candidate:
                count += 1
            elif count > 0:
                count -= 1
            else:
                candidate = i
                count = 1

        return candidate

