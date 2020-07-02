class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]*(num+1)
        for i in range(num+1):
            res[i] = res[int(i/2)] + i%2
        return res
