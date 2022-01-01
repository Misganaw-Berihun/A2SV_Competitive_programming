# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,input().split())
theDict = defaultdict(list)

B = []
#add elements of A
for i in range(1 , n + 1):
    theDict[input()].append(str(i))
#add Elements of B
for j in range(m):
    B.append(input())
for elem in B:
    if elem in theDict.keys():
        print(' '.join(theDict[elem]))
    else:
        print(-1)
