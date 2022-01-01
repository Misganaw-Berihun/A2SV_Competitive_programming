if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
theList = [x for x in arr]
theList.sort();
idx = -2;
while theList[idx] == theList[idx + 1]:
    idx -= 1
print(theList[idx])
