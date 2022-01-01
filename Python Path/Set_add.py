# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
theSet = set()
{theSet.add(input()) for i in range(N)}
print(len(theSet))
