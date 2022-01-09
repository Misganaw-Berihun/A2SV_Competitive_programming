def main():
    t = int(input())#number of testcases

    for i in range(t):
        latin_let = input()
        s = input()
        let_dict = {}
        duration = 0;

        for i,k in enumerate(latin_let):
            let_dict[k] = i

        for i in range(1,len(s)):
            duration += abs(let_dict[s[i]] - let_dict[s[i-1]])

        print(duration)

main()
