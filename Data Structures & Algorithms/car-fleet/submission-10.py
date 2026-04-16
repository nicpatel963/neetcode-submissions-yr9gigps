class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse=True)
        result = []
        for p,s in cars:
            time = (target-p)/s
            if not result or result[-1] < time:
                result.append(time)
            
        return len(result)
            