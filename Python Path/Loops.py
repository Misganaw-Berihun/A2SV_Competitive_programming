if __name__ == '__main__':
    n = int(raw_input())
if n < 1 or n > 20:
    print "must be between 1 and 20(inclusive)"

for i in range(n):
    print i ** 2
