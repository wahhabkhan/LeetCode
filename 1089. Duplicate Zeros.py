class Solution(object):
    def duplicateZeros(self, arr):
      """
      :type arr: List[int]
      :rtype: None Do not return anything, modify arr in-place instead.
      """
      n = len(arr)
      result = []

      for i in range(n):
        if arr[i] == 0:
            result.append(0)
            if len(result) < n:
                result.append(0)
        else:
            result.append(arr[i])
        if len(result) >= n:
            break

      for i in range(n):
        arr[i] = result[i]
                
