class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        total = 0
        sign = 1  # start with positive for most significant digit

        for digit in s:
            total += sign * int(digit)
            sign *= -1  # alternate the sign

        return total
        
