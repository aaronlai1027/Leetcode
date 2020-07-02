class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
            
        
        
#         nums = [0]+nums
#         d = collections.deque()
#         d.append(nums[0])
#         res = float("-inf")
        
#         for i in range(1,len(nums)):
#             nums[i] += nums[i-1]
#             res = max(res,nums[i]-nums[d[0]])
#             while d and nums[i] <= nums[d[-1]]:
#                 d.pop()
#             d.append(i)
#         return res
