def main():
    t = int(input())#number of testcases

    for i in range(t):
        n = int(input())#number of integers
        arr = list(map(int,input().split()))#inputs
        visited = set()

        for num in arr:
            if num not in visited:
                visited.add(num)
            else:
                visited.add(-1 * num)

        print(len(visited))

main()
