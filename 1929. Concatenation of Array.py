class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            nums.insert(i + n , nums[i])

        return nums
        
