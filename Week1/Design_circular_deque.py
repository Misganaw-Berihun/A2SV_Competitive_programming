class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0] * k
        self.front = 0
        self.last = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size != len(self.deque): #is deque full
            self.deque[self.front] = value
            self.front -= 1
            
            if self.front == -1:
                self.front = len(self.deque) - 1
            
            self.size += 1
            return True
        else:
            return False
        
    def insertLast(self, value: int) -> bool:
        if self.size !=  len(self.deque):
            self.last += 1
            if self.last == len(self.deque):
                self.last = 0
                
            self.deque[self.last] = value
            self.size += 1
            return True
        else:
            return False
                
    def deleteFront(self) -> bool:
        if self.size != 0:  #if deque not empty
            self.front += 1
            if self.front == len(self.deque):
                self.front = 0
            self.size -= 1
            return True
        else:
            return False
        
    def deleteLast(self) -> bool:
        if self.size != 0: #if deque not empty
            self.last -= 1
            if self.last == -1:
                self.last = len(self.deque) - 1
                
            self.size -= 1
            return True
        else:
            return False
            

    def getFront(self) -> int:
        if self.size != 0:
            if self.front == len(self.deque) - 1:
                return self.deque[0]
            else:
                return self.deque[self.front + 1]
        else:
            return -1
        

    def getRear(self) -> int:
        if self.size != 0:
            return self.deque[self.last]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == len(self.deque)
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
