# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
nShoes  = int(input())
shoeSizeDict = list(map(int,input().split() ))

sizeDict = Counter(shoeSizeDict)
nCustomers = int(input())

amountMoney = 0;
for i in range(nCustomers):
    size,price = map(int,input().split())


    if size in sizeDict.keys():
        amountMoney += price
        sizeDict[size] -= 1
        if sizeDict[size] == 0:
            sizeDict.pop(size)

print(amountMoney)
