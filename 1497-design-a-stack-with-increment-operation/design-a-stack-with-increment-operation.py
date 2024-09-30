class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize 
        self.countPushed = 0 
        self.stack = []

    def push(self, x: int) -> None:
        if self.countPushed < self.maxSize:
            self.stack.append(x) 
            self.countPushed += 1 

    def pop(self) -> int:
        if not self.stack:
            return -1 
        else:
            popValue = self.stack.pop() 
            self.countPushed -= 1 
        return popValue         
        
    def increment(self, k: int, val: int) -> None:
        if k > self.countPushed:
            k = self.countPushed 
        for i in range(k):
            self.stack[i] += val 
        








# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)