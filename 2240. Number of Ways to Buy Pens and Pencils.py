class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        count = 0
        for pens in range(total // cost1 + 1):
            remaining = total - pens * cost1
            pencils = remaining // cost2
            count += pencils + 1
        return count

        
