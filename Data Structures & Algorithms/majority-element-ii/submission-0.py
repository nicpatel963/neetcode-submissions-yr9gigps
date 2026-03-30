class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        return [key for key,val in freq.items() if val > len(nums)//3]

