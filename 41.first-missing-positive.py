class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
                swap(i,nums[i]-1)
                
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1

