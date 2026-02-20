class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lonely = []
        count = Counter(nums)

        for num in nums:
            if count[num] == 1 and (num - 1) not in count and (num + 1) not in count:
                lonely.append(num)
        
        return lonely


        
