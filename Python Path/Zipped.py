# Enter your code here. Read input from STDIN. Print output to STDOUT
n,x = map(int,input().split())

scores = []
for i in range(x):
    values = list(map(float, input().split()))
    scores.append(values)

scores = list( zip(*scores) )

for row in scores:
    print( sum(row) / x)
