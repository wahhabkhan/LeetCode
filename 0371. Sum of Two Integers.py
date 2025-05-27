class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # Mask to get last 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            # ^ gets the sum without carry
            temp = (a ^ b) & mask
            # & gets the carry, <<1 moves it to the correct position
            b = ((a & b) << 1) & mask
            a = temp

        # If a is negative in 32-bit, convert it to Python's negative number
        return a if a <= MAX else ~(a ^ mask)
        
