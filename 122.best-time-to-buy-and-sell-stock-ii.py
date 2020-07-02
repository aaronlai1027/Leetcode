class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices: return 0
        n = len(prices)
        
        hold = -prices[0]
        sold = 0
        
        for p in prices:
            
            old_hold = hold 
            old_sold = sold
             
            hold = max(sold-p,hold)
            sold = max(hold+p,sold)
        
        return sold
        
        
#         dp = [[0]*2 for _ in range(n)]
        
#         dp[0][1] = -prices[0]
#         dp[0][0] = 0
        
#         for i in range(1,n):
#             dp[i][1] = max(dp[i-1][0]-prices[i],dp[i-1][1])
#             dp[i][0] = max(dp[i-1][1]+prices[i],dp[i-1][0])
        
#         return max(dp[n-1])
