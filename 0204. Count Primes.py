class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0

        is_prime = [True]* n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                # Mark multiples of i as non-prime
                for j in range(i*i, n, i):
                    is_prime[j] = False

        return sum(is_prime)

        #for large value, time limit exceed
        # def is_prime(x):
        #     if x<2:
        #         return False
            
        #     for i in range(2, int(x ** 0.5)+1):
        #         if x%i == 0:
        #             return False
        #     return True

        # count = 0
        # for i in range(2,n):
        #     if is_prime(i):
        #         count += 1

        # return count
