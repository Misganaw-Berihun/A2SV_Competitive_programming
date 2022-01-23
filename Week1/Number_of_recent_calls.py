class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.d = deque()
        

    def ping(self, t: int) -> int:
        self.d.append(t)
        minimum = t - 3000
        
        while self.d and minimum > self.d[0]:
            self.d.popleft()
            
        self.counter = len(self.d)
        
        return self.counter
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
