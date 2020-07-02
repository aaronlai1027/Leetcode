class Solution:
    
# backward
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= target:
                target = i
        return target == 0
    
# forward
    # def canJump(self, nums):
    #     m = 0
    #     for i, n in enumerate(nums):
    #         if i > m:
    #             return False
    #         m = max(m, i+n)
    #     return True
