class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        num = ""
        while x > 0:
            rem = x % 10
            x = x // 10  # use integer division
            num += str(rem)

        # if input was 0, num will be "" → handle that
        rev = int(num) if num else 0
        rev *= sign

        # check 32-bit range
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
            


