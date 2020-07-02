class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        nums = [1]*n
        
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                nums[i] = max(nums[i], nums[i+1] + 1)
                
        return sum(nums)
#         X X X i
#         if i > i-1: k = len+=1,k+len+1
#         else: k=k+1,len=0
