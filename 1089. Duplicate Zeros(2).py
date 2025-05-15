class Solution(object):
    def duplicateZeros(self, arr):
      """
      :type arr: List[int]
      :rtype: None Do not return anything, modify arr in-place instead.
      """
      i = 0
      while i < len(arr):
        if arr[i] == 0:
            # Insert 0 at i+1 and pop last to keep length same
            arr.insert(i + 1, 0)
            arr.pop()
            i += 1  # Skip the duplicated zero
        i += 1
