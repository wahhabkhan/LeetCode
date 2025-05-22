class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for val in str(num):
            digit = int(val)
            if num % digit == 0:
                count += 1
        return count

        
