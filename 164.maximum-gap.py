class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2 or max(nums) == min(nums): return 0
        n = len(nums)
        maxn, minn = max(nums), min(nums)

        
        avg_gap = (maxn - minn)//(n-1) if (maxn - minn)//(n-1) > 0 else 1
        bucket_array = [[None,None] for _ in range((maxn-minn)//avg_gap+1)]
        
        for num in nums:
            idx = (num-minn)//avg_gap
            cell = bucket_array[idx]
            cell[0] = num if not cell[0] else min(cell[0],num)
            cell[1] = num if not cell[1] else max(cell[1],num)

        bucket_array = [b for b in bucket_array if b[0]]

        res = 0
        for i in range(1,len(bucket_array)):
            res = max(res, bucket_array[i][0] - bucket_array[i-1][1])
            
        return res
