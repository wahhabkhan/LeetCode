class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        total = 1 << n # 2^n

        for i in range(total):
            res.append(i ^ (i >> 1))
        return res
        
