class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        i = 1
        while n >= i:
            n -= i
            i += 1
        return i - 1

        
