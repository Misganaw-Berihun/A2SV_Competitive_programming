# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input()) #number of test cases
for i in range(t): #for each test case
    try:
        a,b = map(int,input().split())
        print(a//b)
    except ZeroDivisionError as e1:
        print ("Error Code:",e1)
    except ValueError as e2:
        print ("Error Code:",e2)
