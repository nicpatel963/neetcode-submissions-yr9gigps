class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = [[pos,speed] for pos, speed in zip(position, speed)]
        posAndSpeed = sorted(posAndSpeed, key= lambda i:i[0])
        ans = []
        index = -1
        for i in posAndSpeed:
            time = (target - i[0]) / i[1]
            if index == -1:
                ans.append(time)
                index +=1      
            elif index >= 0 and ans[index] != time:
                while index >-1 and ans[index] < time:
                    ans.pop()
                    index -= 1
                ans.append(time)
                index += 1
        return len(ans)
            

