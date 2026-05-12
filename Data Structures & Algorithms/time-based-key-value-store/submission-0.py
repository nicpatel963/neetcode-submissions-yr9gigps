class TimeMap:

    def __init__(self):
        self.myMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.myMap.get(key,[])
        values.append([timestamp,value])
        self.myMap[key] = values

    def get(self, key: str, timestamp: int) -> str:
        values = self.myMap.get(key,[])
        res = ""
        left,right = 0,len(values)-1
        while left <= right:
            mid = left + right - left // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res
