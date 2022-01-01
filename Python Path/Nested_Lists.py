if __name__ == '__main__':
    theList = [];
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        theList.append([name,score])
    theList.sort(key = lambda row : row[1])
    idx = 1
    while theList[idx][1] == theList[idx - 1][1]:
        idx += 1
    scndLowest = [theList[idx][0]]
    while idx != len(theList) - 1 and theList[idx][1] == theList[idx + 1][1]:
        scndLowest.append(theList[idx + 1][0])
        idx += 1
    scndLowest.sort()

    for x in scndLowest:
        print x

    
