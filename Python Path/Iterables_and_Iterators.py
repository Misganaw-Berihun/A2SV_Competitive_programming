from itertools import combinations

N = int(input())
letters = input().split()
k = int(input())
a_count = 0;
theList = list(combinations(letters, k))

for tup in theList:
    if 'a' in tup:
        a_count += 1
print(round(a_count/len(theList), 3))
