import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. Check if n is a perfect square
        if int(math.sqrt(n))**2 == n:
            return 1

        # 2. Check if sum of 2 squares
        for i in range(1, int(math.sqrt(n)) + 1):
            j = n - i * i
            if int(math.sqrt(j))**2 == j:
                return 2

        # 3. Legendre's 3-square theorem
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4

        # 4. Otherwise
        return 3
