class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for i in nums:
            temp[i] = temp.get(i,0) + 1
        sorted_temp = sorted(temp.keys(), key= lambda i: temp[i], reverse=True)
        return sorted_temp[:k]
            
