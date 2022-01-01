# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,k = input().split()
[print (''.join(item)) for item in permutations(sorted(s),int(k))]
