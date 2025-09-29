class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        #Two Pointers
        a = 0
        b = int(c ** 0.5)
        while a <= b:
          sum = a ** 2 + b ** 2
          if sum == c:
            return True
          elif sum < c:
            a += 1
          else:
            b -= 1
        return False

        #Brute Force
        # for a in range(0, int(c ** 0.5)+1):
        #     b2 = c - a ** 2
        #     b = int(b2 ** 0.5)
        #     if b*b == b2:
        #         return True
        # return False




        
