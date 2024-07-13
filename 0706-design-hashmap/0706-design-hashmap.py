class LinkedList:
    def __init__(self,value=None,key=None,next=None):
        self.key=key
        self.value=value
        self.next=next

class MyHashMap:

    def __init__(self):
        self.map=[LinkedList() for i in range(1000)]

    def hash(self,value):
        return value%len(self.map)
    def put(self, key: int, value: int) -> None:
        cur=self.map[self.hash(key)]
        while cur.next:
            if(cur.next.key==key):
                cur.next.value=value
                return 
            cur=cur.next
        cur.next=LinkedList(value,key)


    def get(self, key: int) -> int:
        cur=self.map[self.hash(key)]
        while cur:
            if(cur.key==key):
                return cur.value
            cur=cur.next
        return -1
    

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if(cur.next.key==key):
                cur.next=cur.next.next
                return
            cur=cur.next
        
        return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)