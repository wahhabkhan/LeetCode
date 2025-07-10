class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        hex_map = "0123456789abcdef"
        result = ""

        num &= 0xFFFFFFFF

        while num>0:
            remainder = num % 16
            result = hex_map[remainder] + result
            num //= 16

        return result
        
