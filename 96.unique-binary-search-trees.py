class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            for left in range(i):
                right = i - 1 - left
                dp[i] += dp[left] * dp[right]
        return dp[-1]
