class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        num = 0
        sign = 1  # +1 for positive, -1 for negative

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # handle multi-digit numbers
            elif char in "+-":
                res += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif char == ")":
                res += sign * num
                num = 0
                res *= stack.pop()  # sign before '('
                res += stack.pop()  # result calculated before '('
        
        return res + sign * num
