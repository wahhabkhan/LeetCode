class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        C = collections.Counter
        return list((C(nums1) & C(nums2)).elements())
        
