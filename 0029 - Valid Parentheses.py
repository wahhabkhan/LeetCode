class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket = { ')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in bracket:
                top = stack.pop() if stack else '#'
                
                if bracket[char] != top:
                    return False

            else:
                stack.append(char)
        return not stack
