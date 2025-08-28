class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        for i in range(len(nums)):
            # count = 0
            # while nums[i]>0:
            #     nums[i] &= (nums[i]-1)
            #     count += 1
            if bin(i).count("1") == k:
                total += nums[i]
        return total
