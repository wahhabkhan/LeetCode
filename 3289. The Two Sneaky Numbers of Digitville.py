class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        duplicate = []
        seen = set(nums)
        for num in nums:
            if num not in result:
                result.append(num)
            else:
                duplicate.append(num) 
        return duplicate

        '''    
        sneaky = []
        for num in nums:
          idx = abs(num)
          if nums[idx] < 0:
            sneaky.append(idx)  # seen before → duplicate
          else:
            nums[idx] = -nums[idx]  # mark visited
        return sneaky
        '''
