class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        ans = 0
        
        for elem in ops: #for each elem in ops
            if elem.isdigit() or elem.lstrip('-').isdigit(): 
                stack.append(int(elem))
            elif elem == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                
                stack.append(num2)
                stack.append(num1)
                stack.append(num1 + num2)
            elif elem == 'C':
                stack.pop()
            elif elem == 'D':
                num = stack.pop()
                stack.append(num)
                stack.append(num * 2)
                
        while len(stack) != 0:
            ans += stack.pop()
            
        return ans
