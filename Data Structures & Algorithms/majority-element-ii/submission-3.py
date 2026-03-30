class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count,limit = 0,len(nums)//3
        prev = None
        nums.sort(reverse=True)
        result = set()
        for i in nums:
            if prev == i:
                count += 1
            else:
                count = 1
                prev = i

            if count > limit:
                result.add(i)
                count = 0
                
        return list(result)