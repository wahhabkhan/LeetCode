class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0

        for j in range(1, n - 1):
           max_i = max(nums[:j])        # i < j
           max_k = max(nums[j + 1:])    # k > j
           val = (max_i - nums[j]) * max_k
           res = max(res, val)

        return max(0, res)  # return 0 if all values are negative

        
