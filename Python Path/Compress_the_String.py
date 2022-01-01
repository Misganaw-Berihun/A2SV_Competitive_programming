# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
s = input();
key_fun = lambda a : a

for key,value in itertools.groupby(s,key_fun):
    print("(",len(list(value)) , ", ", key, ")" ,end = " " ,sep = "")
Iterables and Iterators`
