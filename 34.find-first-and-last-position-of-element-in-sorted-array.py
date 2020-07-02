class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.lowerbound(nums, target)
        right = self.upperbound(nums, target)
        if right == left:
            return [-1,-1]
        return [left, right-1]
    
    def lowerbound(self, nums, target):
        left, right = 0, len(nums)
        
        while left < right:
            mid = left + (right - left)//2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
    
    def upperbound(self, nums, target):
        left, right = 0, len(nums)
        
        while left < right:
            mid = left + (right - left)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
