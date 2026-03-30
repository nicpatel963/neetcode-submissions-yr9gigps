class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0, len(nums)-1
        while i<=j:
            if nums[j] == val:
                j-=1
            elif nums[i] != val:
                i +=1
            else:
                nums[i] = nums[j]
                i+=1
                j-=1
        return j+1