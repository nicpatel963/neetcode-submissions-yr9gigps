class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longSeq = set()
        for i in nums:
            if i-1 not in nums:
                tempSeq = set()
                while True:
                    tempSeq.add(i)
                    if i+1 not in nums:
                        if len(tempSeq) > len(longSeq):
                            longSeq = set(tempSeq)
                        break
                    i += 1
        return len(longSeq)