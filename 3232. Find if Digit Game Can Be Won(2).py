class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        single_sum = sum(num for num in nums if num < 10)
        double_sum = sum(num for num in nums if num >= 10)
        total_sum = sum(nums)
        
        # Alice wins if single_sum > rest or double_sum > rest
        return single_sum > (total_sum - single_sum) or double_sum > (total_sum - double_sum)
        
