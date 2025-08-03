class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.orignal = nums[:]
        

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.orignal

    def shuffle(self):
        """
        :rtype: List[int]
        """
        shuffled = self.nums[:]
        for i in range(len(shuffled)-1, 0, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
