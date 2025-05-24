class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sum_digit(n):
            total = 0
            while n>0:
                total += n%10
                n //= 10
            return total

        return min(sum_digit(n) for n in nums) 
        
