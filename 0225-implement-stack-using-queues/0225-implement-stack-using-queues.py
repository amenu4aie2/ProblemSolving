class MyStack:

    def __init__(self):
        
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack1.append(x)
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        

    def pop(self) -> int:
        return self.stack2.pop() if self.stack2 else[]

    def top(self) -> int:
        return self.stack2[-1] if self.stack2 else []
        

    def empty(self) -> bool:
        return False if self.stack2 else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()