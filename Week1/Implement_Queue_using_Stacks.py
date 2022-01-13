#https://leetcode.com/problems/implement-queue-using-stacks
class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def move_1_2(self):
        while(len(self.stack_1) != 0):
            self.stack_2.append(self.stack_1.pop())

    def move_2_1(self):
        while(len(self.stack_2) != 0):
            self.stack_1.append(self.stack_2.pop())

    def pop(self) -> int:
        if len(self.stack_1) != 0:
            self.move_1_2()

        temp = self.stack_2.pop()
        self.move_2_1()

        return temp

    def peek(self) -> int:
        if len(self.stack_1) != 0:
            self.move_1_2()

        temp = self.stack_2.pop()
        self.stack_2.append(temp)
        self.move_2_1()

        return temp


    def empty(self) -> bool:
        return len(self.stack_1) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
