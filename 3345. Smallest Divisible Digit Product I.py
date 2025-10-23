class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            s = str(n)
            if '0' in s:
                return n
                
            prod = 1
            for ch in s:
                prod *= int(ch)

            # Check divisibility
            if prod % t == 0:
                return n

            # Increment and continue
            n += 1


        
