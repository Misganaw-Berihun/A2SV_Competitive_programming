from collections import namedtuple

n = int(input())
std = namedtuple("Student",' '.join(list(input().split(' '))) )
total = 0
for i in range(n):
    s1 = std( *list(input().split()))
    total += int(s1.MARKS)

print( total/ n)
