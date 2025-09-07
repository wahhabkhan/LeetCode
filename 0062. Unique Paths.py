import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n

        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]
        # N = m + n - 2   # total moves
        # R = min(m-1, n-1)  # choose smaller one
        # res = 1
        
        # for i in range(1, R+1):
        #     res = res * (N - R + i) // i
        
        # return res
