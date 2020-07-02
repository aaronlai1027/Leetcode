class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        if k >= n / 2:
            res = 0
            for i in range(1,n):
                if prices[i] > prices[i-1]:
                    res = res + prices[i] - prices[i-1]
            return res
       
        hold = [float('-inf')]*(k+1)
        sold = [float('-inf')]*(k+1)
        
        hold[0] = 0
        sold[0] = 0
        
        for i in range(0,n):
            
            old_hold = hold
            old_sold = sold
            
            for j in range(1,k+1):
                
                hold[j] = max(old_sold[j-1]-prices[i],old_hold[j])
                sold[j] = max(old_hold[j]+prices[i],old_sold[j])
                
        # print(dp)
        return max(sold)
