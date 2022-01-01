# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,k = input().split()
for i in range(1,int(k)+1):
    [print (''.join(items)) for items in combinations(sorted(s),i)]
