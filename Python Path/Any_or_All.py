# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
    n = int(input())
    num_list = list(map(int,input().split()))

    is_positive_list = list(map(lambda a: a > 0,num_list))
    a_palindrome = list(map(lambda a : str(a) == str(a)[::-1], num_list))

    print(all(is_positive_list) and any(a_palindrome))


main()
