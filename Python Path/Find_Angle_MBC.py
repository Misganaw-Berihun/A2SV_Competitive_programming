# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
import math

AB = int(input())
BC = int(input())

AC = math.hypot(AB,BC)
MC = AC / 2
ang_BCA = math.atan(AB/BC)
BM = math.sqrt(BC ** 2 + MC ** 2 - 2 * BC * MC * math.cos(ang_BCA))
theta = math.asin( MC * math.sin(ang_BCA) / BM)
theta = math.degrees(theta)
print(round(theta),u"\N{DEGREE SIGN}", sep = '')
