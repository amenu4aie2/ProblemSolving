class MyHashSet:

    def __init__(self) -> None:
      self.lis = [None] * 1000

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        index = key % 1000
        if self.lis[index] is None:
            self.lis[index] = [key]
        else:
            self.lis[index].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        index = key % 1000
        self.lis[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % 1000
        if self.lis[index] is None:
            return False
        return key in self.lis[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)