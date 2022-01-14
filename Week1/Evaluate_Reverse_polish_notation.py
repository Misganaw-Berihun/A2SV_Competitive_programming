class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i].isdigit()  \
                        or tokens[i].lstrip('-').isdigit():
                stack.append(int(tokens[i]))
            else:
                num_2 = stack.pop()
                num_1 = stack.pop()

                if tokens[i] == '+':
                    stack.append(num_1 + num_2)
                elif tokens[i] == '*':
                    stack.append(num_1 * num_2)
                elif tokens[i] == '/':
                    stack.append(int(num_1 / num_2))
                elif tokens[i] == '-':
                    stack.append(num_1 - num_2)

        return stack.pop()
