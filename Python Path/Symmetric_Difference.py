# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
first_set = set(map(int,input().split()))
n = int(input())
second_set = set(map(int,input().split()))

aUb = first_set.union(second_set) #a union b
anb = first_set.intersection(second_set) # a intersection b
a_diff_b = aUb.difference(anb)
#difference(first_set.intersection(second_set))
mylist = list(a_diff_b)
mylist.sort()
for x in mylist:
    print (x)
