# Enter your code here. Read input from STDIN. Print output to STDOUT
def compare(ch):
    return [
            ch.isdigit(),
            ch.isupper(),
            ch.isdigit() and int(ch) % 2 == 0,
            ord(ch)
            ]

def main():
    s = input()
    sorted_s = sorted(s,key = compare)
    print(''.join(sorted_s))

main()
