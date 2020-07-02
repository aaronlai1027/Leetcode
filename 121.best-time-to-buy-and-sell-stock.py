class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxCur = 0
        maxSofar = 0
        for i in range(1,len(prices)):
            maxCur += prices[i] - prices[i-1]
            maxCur = max(0,maxCur)
            maxSofar = max(maxSofar,maxCur)
        return maxSofar
