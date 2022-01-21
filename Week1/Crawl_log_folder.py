class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        
        for elem in logs:
            ch = elem[:len(elem) - 1]
            
            if ch.isalnum():
                stack.append(ch)
            elif ch == '..' and stack:
                stack.pop()
        
        return len(stack)
