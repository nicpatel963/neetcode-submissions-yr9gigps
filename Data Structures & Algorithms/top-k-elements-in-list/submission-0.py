class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for i in nums:
            if i not in temp:
                temp[i]=nums.count(i)
        sorted_temp = {k:v for k,v in sorted(temp.items(), key = lambda item:item[1], reverse=True)}
        ans = []
        print(sorted_temp)
        for i in range(k):
            ans.append(list(sorted_temp.keys())[i])
        return ans
            
