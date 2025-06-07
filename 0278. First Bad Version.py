class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # Bad version, but could be the first
            else:
                left = mid + 1  # First bad version must be after mid
        
        return left
