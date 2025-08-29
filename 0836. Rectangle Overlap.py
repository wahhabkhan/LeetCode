class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        if x2 <= a1 or a2 <= x1:
            return False
        if y2 <= b1 or b2 <= y1:
            return False

        return True
        
        
