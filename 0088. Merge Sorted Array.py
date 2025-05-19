class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # Last element of real nums1
        j = n - 1  # Last element of nums2
        k = m + n - 1  # Last index of nums1's total space

        while i >= 0 and j >= 0:
          if nums1[i] > nums2[j]:
             nums1[k] = nums1[i]
             i -= 1
          else:
             nums1[k] = nums2[j]
             j -= 1
          k -= 1 
        # Copy remaining nums2
        while j >= 0:
          nums1[k] = nums2[j]
          k -= 1
          j -= 1


        
