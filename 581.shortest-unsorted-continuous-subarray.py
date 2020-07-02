class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = -1
        end = -2
        tmax = nums[0]
        tmin = nums[len(nums)-1]
        for i in range(1,len(nums)):
            tmax = max(tmax,nums[i])
            tmin = min(tmin,nums[len(nums)-i])
            if nums[i] < tmax:
                end = i
            if nums[len(nums)-1-i] > tmin:
                start = len(nums)-1-i
        return end - start + 1
            
