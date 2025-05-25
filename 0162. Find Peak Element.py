class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid  # Peak is in left half (including mid)
            else:
                left = mid + 1  # Peak is in right half

        return left  # or return right (both are same here)
        
