class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            result["".join(sorted(s))] = result.get("".join(sorted(s)),[]) + [s]
        
        return list(result.values())