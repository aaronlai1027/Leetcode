class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 0
        second = None
        for i in range(len(nums)):
            if nums[i] < nums[first]:
                first = i
            elif nums[i] > nums[first]:
                if second and nums[i] > nums[second]:
                    return True
                else:
                    second = i
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(nums)
#         dp = [1]*n
#         for i in range(n):
#             for j in range(i,-1,-1):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i],dp[j]+1)
        
#         for i in dp:
#             if i >= 3:
#                 return True
#         return False
