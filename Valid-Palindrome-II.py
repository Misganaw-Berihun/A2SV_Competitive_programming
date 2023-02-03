class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r :
            if s[l] != s[r]:
                cond1 = (s[l: r - 1] == s[r - 1 : l : -1])
                cond2 = (s[l + 1: r] == s[r : l + 1: -1])
                
                return cond1 or cond2
            l += 1
            r -= 1
            
        return True
