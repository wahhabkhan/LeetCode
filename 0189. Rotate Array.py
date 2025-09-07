class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def rev(l,r):
            while(l<r):
                nums[l],nums[r] = nums[r],nums[l]
                l,r = l+1, r-1


        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
