class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        list = set()
        for num in nums:
            if num in list:
                return True
            list.add(num)
