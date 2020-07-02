class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k=2       
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
