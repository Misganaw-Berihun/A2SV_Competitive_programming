class Solution:
    def isValid(self, s: str) -> bool:
        theStack = []
        check_list = { '(' :')','[':']','{':'}' }

        for i in range(len(s)):
            if s[i] in check_list.keys():
                theStack.append(s[i])
            else:
                if len(theStack) != 0:
                    ch = theStack.pop()

                    if s[i] != check_list[ch]:
                        return False

                else:
                    return False

        return len(theStack) == 0

        
