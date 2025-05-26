class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        i = 1
        
        while i < len(nums) - 1:
            # Skip if current equals previous (to avoid double counting plateaus)
            if nums[i] == nums[i - 1]:
                i += 1
                continue

            # Find closest non-equal neighbors
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            right = i + 1
            while right < len(nums) and nums[right] == nums[i]:
                right += 1

            if left >= 0 and right < len(nums):
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    count += 1  # Hill
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    count += 1  # Valley
            
            i = right  # Move `i` to `right` to skip plateau

        return count
        
