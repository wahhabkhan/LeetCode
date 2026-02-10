class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = Counter(nums)
        for key,value in freq.items():
            if value > 2:
                return False
        return True 
        
