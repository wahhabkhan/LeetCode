class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))
        
