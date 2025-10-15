        n = len(nums)
        # dp[j] will eventually store dp[i][j] for the current i in outer loop
        dp = [0] * n

        # iterate start index i from rightmost to leftmost
        for i in range(n - 1, -1, -1):
            dp[i] = nums[i]              # base case dp[i][i] = nums[i]
            for j in range(i + 1, n):    # expand the end index j to the right
                # if current player picks nums[i], opponent's result is dp[j] (which is dp[i+1][j])
                pick_left  = nums[i] - dp[j]
                # if current player picks nums[j], opponent's result is dp[j-1] (which is dp[i][j-1])
                pick_right = nums[j] - dp[j - 1]
                dp[j] = max(pick_left, pick_right)
        # dp[n-1] is dp[0][n-1] after finishing
        return dp[n - 1] >= 0
