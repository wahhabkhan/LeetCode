class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Frequency count
        freq = Counter(nums)
    
        # Step 2: Create buckets
        bucket = [[] for i in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
    
        # Step 3: Gather top k frequent elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # start from high frequency
           for num in bucket[i]:
              result.append(num)
              if len(result) == k:
                 return result       
        
