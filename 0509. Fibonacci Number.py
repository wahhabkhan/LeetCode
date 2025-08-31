class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        # return self.fib(n-1) + self.fib(n-2)
        
        a,b = 0,1
        for i in range(2, n+1):
            a,b = b , a+b
        return b
