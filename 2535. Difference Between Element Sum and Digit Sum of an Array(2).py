class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total_element = 0
        total_digit = 0
        
        for num in nums:
            total_element += num
            n = num
            while n > 0:
                total_digit += n % 10
                n //= 10
        
        return abs(total_element - total_digit)
