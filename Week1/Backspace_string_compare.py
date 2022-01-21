lass Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        equal = True
        
        #push element of s to stack1 if it is not # or
        #pop element from stack1 if # 
        for ch in s:
            if stack1 and ch =="#":
                stack1.pop()
            elif ch != "#":
                stack1.append(ch)
                
        #push element of t to stack2 if it is not # or 
        #pop element from stack2 if #
        for c in t:
            if stack2 and c =="#":
                stack2.pop()
            elif c != "#":
                stack2.append(c)
            
        #compare elements of stack1 and stack2 if different equal = false
        while stack1 and stack2:
            if stack1.pop() != stack2.pop():
                equal = False
                
        #if one of the stacks is not empty
        if stack1 or stack2:
            equal = False
        
        return equal
                
