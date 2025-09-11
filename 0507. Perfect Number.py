class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1: 
            return False
        divisors = [1]
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        return sum(divisors) == num
        # if num < 1:
        #     return False
        # n = num // 2
        # divisors = []
        # for i in range(1,n+1):
        #     if num % i == 0:
        #         divisors.append(i)
        # return True if sum(divisors) == num else False 
        
