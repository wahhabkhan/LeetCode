class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(reversed(result))
        
