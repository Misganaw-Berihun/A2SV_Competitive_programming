import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
if n < 1 or n > 100:
    print "above range"
if n % 2 == 1:
    print "Weird"
else:
    if (n >= 2 and n <= 5) or (n > 20) :
        print "Not Weird"
    else:
        print "Weird"
