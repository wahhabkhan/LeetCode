class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num % 2 == 0:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        
        if not freq:
            return -1

        max_freq = -1
        result = -1

        for num in freq:
            if freq[num] > max_freq or (freq[num] == max_freq and num < result):
                max_freq = freq[num]
                result = num

        return result
     
         
        
