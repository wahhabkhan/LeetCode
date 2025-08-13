class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set(nums)

        missing = [i for i in range(1,len(nums)+1) if i not in seen] 

        return missing
