# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

oDict = OrderedDict();

n = int(input())
for i in range(n):
    itemList = input().split()
    price = int(itemList[-1])
    desc = ' '.join(itemList[:(len(itemList) - 1)])
    if desc in oDict:
        oDict[desc] += price
    else:
        oDict[desc] = price

for el,pr in oDict.items():
    print (el + " " + str(pr) )
