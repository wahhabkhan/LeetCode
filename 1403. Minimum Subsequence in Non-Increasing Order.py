class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        total = sum(nums)
        subsequence = []
        subseq_sum = 0

        for num in nums:
            subsequence.append(num)
            subseq_sum += num
            if subseq_sum > total - subseq_sum:
                break
        
        return subsequence
        
