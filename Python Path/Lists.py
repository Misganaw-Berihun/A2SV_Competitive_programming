if __name__ == '__main__':
    N = int(input())
    theList = []
    for i in range(N):
        line = input()
        aList =[]
        aList = line.split();
        command = aList[0]
        if command == "insert":
            theList.insert(int(aList[1]),int(aList[2]))
        elif command == "print":
            print(theList)
        elif command == "remove":
            theList.remove(int(aList[1]))
        elif command == "append":
            e = int(aList[1])
            theList.append(e)
        elif command == "sort":
            theList.sort()
        elif command == "pop":
            theList.pop()
        elif command == "reverse":
            theList.reverse()
