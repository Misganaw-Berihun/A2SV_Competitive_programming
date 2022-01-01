# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
theList = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))

happiness = 0;

for item in theList:
    if item in a:
        happiness += 1
    if item in b:
        happiness -= 1

print(happiness)
