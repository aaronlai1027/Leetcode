class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumGas, sumCost, tank = 0, 0, 0
        res = 0
        for i in range(len(gas)):
            sumGas += gas[i]
            sumCost += cost[i]
            tank += gas[i] - cost[i] 
            if tank >= 0:
                continue
            else:
                res = i+1
                tank = 0
        if sumGas >= sumCost:
            return res
        else:
            return -1
