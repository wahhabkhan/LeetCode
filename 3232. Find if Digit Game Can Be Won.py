class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        single_dig_sum = 0
        double_dig_sum = 0
        for num in nums:
            if num>=0 and num<10:
                single_dig_sum += num
            else:
                double_dig_sum += num
        if single_dig_sum != double_dig_sum:
            return True
        else:
            return False

        
