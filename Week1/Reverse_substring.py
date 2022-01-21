class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack1 = []
        
        for let in s:
            reversed_ = ""
            if let == ")":
                ch = stack1.pop()
                
                while ch != "(":
                    reversed_ += ch
                    ch = stack1.pop()
                    
                for c in reversed_:
                    stack1.append(c)
                    
            else:
                stack1.append(let)
        
        return ''.join(stack1)
