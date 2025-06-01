class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1
        return count

# from collections import Counter

# def unequalTriplets(nums):
#     freq = Counter(nums)
#     unique_vals = list(freq.values())
    
#     total = 0
#     left = 0  # total elements before current
#     n = len(nums)
    
#     for count in unique_vals:
#         right = n - left - count  # elements after current group
#         total += left * count * right  # choose one from each group
#         left += count  # move to next group
    
#     return total

        
