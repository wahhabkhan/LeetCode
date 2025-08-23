class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # INT_MAX = 2**31 - 1
        # INT_MIN = -2**31

        # # Edge case: overflow
        # if dividend == INT_MIN and divisor == -1:
        #     return INT_MAX

        # # Work with positive numbers
        # negative = (dividend < 0) ^ (divisor < 0)  # XOR → True if signs differ
        # dividend, divisor = abs(dividend), abs(divisor)

        # result = 0
        # # Repeatedly subtract divisor
        # while dividend >= divisor:
        #     dividend -= divisor
        #     result += 1

        # if negative:
        #     result = -result

        # # Clamp to 32-bit signed integer range
        # return max(INT_MIN, min(INT_MAX, result))

        # Constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle edge case overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        # Subtract divisor multiples using bit shifts
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        # Clamp to 32-bit range
        return max(min(quotient, INT_MAX), INT_MIN)
