class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        result = 0
        temp = {0:1}

        for i in nums:
            prefixSum += i
            currSum = prefixSum - k
            result += temp.get(currSum,0)
            temp[prefixSum] = temp.get(prefixSum,0) + 1

        return result