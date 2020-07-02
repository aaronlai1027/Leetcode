class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        d = collections.deque()
        dp = [float("-inf")]*len(nums)
        for i, n in enumerate(nums):
            if d:
                dp[i] = max(dp[d[0]]+n,n)
            else:
                dp[i] = n
            
            while d and dp[i] >= dp[d[-1]]:
                d.pop()
            d.append(i)
            if d[0] <= i-k:
                d.popleft()
        return max(dp)
            
# Xd[XXX] i

# dp[i] = max(dp[i],d[0]+dp[i])
