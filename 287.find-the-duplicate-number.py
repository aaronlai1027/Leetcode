class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[nums[0]]
        slow = nums[0]
        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]
            
        slow = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return fast
        
        
        
        
        
        
        
        
        
        
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
