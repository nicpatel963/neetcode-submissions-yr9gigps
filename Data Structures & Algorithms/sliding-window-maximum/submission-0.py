class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxNum = nums[0]
        l = 0
        window = []
        for i in range(k):
            maxNum = nums[i] if nums[i] > maxNum else maxNum
            window.append(nums[i])
        res.append(maxNum)

        for r in range(k,len(nums)):
            window.remove(nums[l])
            window.append(nums[r])

            if nums[l] != maxNum:
                maxNum = max(maxNum,nums[r])
            else:
                maxNum = max(window)
            res.append(maxNum)
            
            l += 1
        return res