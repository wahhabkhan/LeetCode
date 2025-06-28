class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        count_L = moves.count('L')
        count_R = moves.count('R')
        count_ = moves.count('_')
    
        return abs(count_R - count_L) + count_
        
