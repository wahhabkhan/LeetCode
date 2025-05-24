class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums:
            for digit in str(n):
               result.append(int(digit))
        return result
            
        
