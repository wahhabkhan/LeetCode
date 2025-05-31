class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')
        n = len(nums)
    
        for i in range(n - 2):
           left, right = i + 1, n - 1
        
           while left < right:
              total = nums[i] + nums[left] + nums[right]
            
              # If this sum is exactly the target, return immediately
              if total == target:
                  return total
            
              # Update closest if this total is better
              if abs(total - target) < abs(closest - target):
                  closest = total
            
              # Move pointers
              if total < target:
                  left += 1
              else:
                  right -= 1
    
        return closest
        
