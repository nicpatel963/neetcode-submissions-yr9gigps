class MyHashSet:

    def __init__(self):
        self.hashSet = {}

    def add(self, key: int) -> None:
        self.hashSet[key] = key
        return None

    def remove(self, key: int) -> None:
        self.hashSet.pop(key) if key in self.hashSet else None
        return None

    def contains(self, key: int) -> bool:
        return True if self.hashSet.get(key) else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)