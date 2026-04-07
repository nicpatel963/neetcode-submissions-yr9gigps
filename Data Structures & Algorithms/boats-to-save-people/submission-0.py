class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        low,high = 0,len(people)-1
        result = 0
        while low <= high:
            total = people[low] + people[high]
            if total <= limit:
                result += 1
                low +=1
                high -= 1
            else:
                result += 1
                high -= 1
            
        return result