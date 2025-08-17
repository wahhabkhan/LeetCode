class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax = curMin = result = nums[0]

        for i in range(1, len(nums)):
            val = nums[i]
            # If negative, swap max and min before calculation
            if val < 0:
                curMax, curMin = curMin, curMax

            curMax = max(val, curMax * val)
            curMin = min(val, curMin * val)

            result = max(result, curMax)

        return result
