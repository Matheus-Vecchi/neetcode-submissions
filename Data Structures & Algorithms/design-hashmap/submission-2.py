class MyHashMap:

    def __init__(self):
        self.obj = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.obj)):
            if key == self.obj[i][0]:
                self.obj[i][0] = key
                self.obj[i][1] = value
                return
        
        self.obj.append([key, value])
        

    def get(self, key: int) -> int:
        for i in range(len(self.obj)):
            if key == self.obj[i][0]:
                return self.obj[i][1]
        
        return -1
        

    def remove(self, key: int) -> None:
        for i in range(len(self.obj)):
            if key == self.obj[i][0]:
                self.obj.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)