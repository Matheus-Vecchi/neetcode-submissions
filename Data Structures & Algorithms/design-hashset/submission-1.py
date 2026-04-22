class MyHashSet:

    def __init__(self):
        self.obj = []        

    def add(self, key: int) -> None:
        for i in self.obj:
            if key == i:
                return
        
        self.obj.append(key)

    def remove(self, key: int) -> None:
        for i in self.obj:
            if key == i:
               self.obj.remove(i)

    def contains(self, key: int) -> bool:
        for i in self.obj:
            if i == key:
                return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)