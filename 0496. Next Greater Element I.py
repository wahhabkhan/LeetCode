class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        stack = []
        next_greater = {}
        
        for num in nums2:
            # While the current number is greater than the stack's top,
            # it is the "next greater" for stack[-1]
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        # Remaining elements in stack have no greater element
        for num in stack:
            next_greater[num] = -1

        # Build result for nums1 based on the mapping
        return [next_greater[num] for num in nums1]

        
