class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        is_negative = num < 0
        num = abs(num)

        result = []
        while num>0:
            result.append(str(num%7))
            num //= 7

        base7 = ''.join(reversed(result))
        return '-' + base7 if is_negative else base7
        
