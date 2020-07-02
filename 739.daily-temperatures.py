class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        stack = []
        
        for i ,t in enumerate(T):
            while stack and  t > stack[-1][0]:
                last_i = stack.pop()[1]
                res[last_i] = i - last_i
            stack.append((t,i))
        
        return res

