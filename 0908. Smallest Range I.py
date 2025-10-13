class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_num = max(nums)
        min_num = min(nums)

        return max(0, (max_num - min_num) - 2 * k)
        
