class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0  # start point

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # obstacle → no path
                elif j > 0:
                    dp[j] += dp[j-1]  # add paths from left
        return dp[-1]
