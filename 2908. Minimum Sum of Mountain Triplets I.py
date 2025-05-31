class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_sum = float('inf')
    
        for i in range(n):
           for j in range(i + 1, n):
              if nums[i] < nums[j]:
                for k in range(j + 1, n):
                    if nums[k] < nums[j]:
                        triplet_sum = nums[i] + nums[j] + nums[k]
                        min_sum = min(min_sum, triplet_sum)
    
        return min_sum if min_sum != float('inf') else -1       
        
