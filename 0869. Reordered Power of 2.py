class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count_n = Counter(str(n))

        for i in range(31):
            if Counter(str(1 << i)) == count_n:
                return True

        return False

        
