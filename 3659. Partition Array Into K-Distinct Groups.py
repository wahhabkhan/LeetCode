class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)

        if n % k != 0:
            return False

        groups = n // k

        freq = Counter(nums)

        if max(freq.values()) > groups:
            return False

        return True
        
        
