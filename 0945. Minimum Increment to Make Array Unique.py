class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        moves = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                needed = prev + 1
                moves += needed - nums[i]
                prev = needed
            else:
                prev = nums[i]

        return moves


        
