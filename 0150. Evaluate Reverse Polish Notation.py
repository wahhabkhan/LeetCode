class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # '/'
                    # use int() to truncate toward zero
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(token))
        return stack[0]


        
