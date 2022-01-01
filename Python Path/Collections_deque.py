# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input()) #number of operations

d = deque()
for i in range(n): # for n operations
    de_list = input().split()
    if(de_list[0] == "append"):
        d.append(int(de_list[1]) )
    elif(de_list[0] == "pop"):
        d.pop()
    elif (de_list[0] == "popleft"):
        d.popleft()
    elif (de_list[0] == "appendleft"):
        d.appendleft(int(de_list[1]));

print(" ".join(list(map(str,d))) )
