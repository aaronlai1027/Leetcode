class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n < 2:
            return 0
        if n == 2:
            return max(0,prices[1]-prices[0])
        
        hold = [float('-inf')]*n
        sold = [float('-inf')]*n
        
        hold[0] = -prices[0]
        hold[1] = max(-prices[0],-prices[1])
        sold[0] = 0
        sold[1] = max(0,hold[0]+prices[1])
        
        for i in range(2,n):
            hold[i] = max(hold[i-1],sold[i-2]-prices[i])
            sold[i] = max(sold[i-1],hold[i-1]+prices[i])
        print(hold,sold)
        return max(sold)
        
