class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1, cand2, count1, count2 = None, None, 0, 0
        for num in nums:
          if num == cand1:
            count1 += 1
          elif num == cand2:
            count2 += 1
          elif count1 == 0:
            cand1, count1 = num, 1
          elif count2 == 0:
            cand2, count2 = num, 1
          else:
            count1 -= 1
            count2 -= 1

        result = []
        for cand in [cand1, cand2]:
          if cand is not None and nums.count(cand) > len(nums)//3:
            result.append(cand)
        return result
        
