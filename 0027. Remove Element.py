class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k

a = Solution()
a.removeElement([1,2,2,3,4,0], 2)
