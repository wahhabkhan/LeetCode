class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)

        pairs = 0
        leftovers = 0

        for c in count.values():
            pairs += c//2
            leftovers += c%2

        return [pairs,leftovers]
        
