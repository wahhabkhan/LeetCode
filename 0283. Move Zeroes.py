class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_pos = 0  # pointer to place the next non-zero element

        # Step 1: Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos] = nums[i]
                non_zero_pos += 1

        # Step 2: Fill the rest of the array with zeroes
        for i in range(non_zero_pos, len(nums)):
            nums[i] = 0
                
