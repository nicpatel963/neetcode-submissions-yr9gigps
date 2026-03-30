class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = target - numbers[i]
            jIndex = numbers.index(j) if j in numbers else 0
            if numbers[i] != j and i < jIndex and j in numbers:
                return [i+1,jIndex+1]
        