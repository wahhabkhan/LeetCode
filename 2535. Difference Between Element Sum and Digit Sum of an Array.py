class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total_element = 0
        for num in nums:
            total_element += num

        total_digit = 0
        for num in nums:
            if num > 9:
                s = sum(int(d) for d in str(num))
                total_digit += s 
            else:
                total_digit += num

        return abs(total_element - total_digit)
