class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        if len(nums)<3:
            return len(nums)
        for i in range(len(nums)):
            if i > count:
                nums[count] = nums[i]
            if nums[count] > nums[count-2] or count < 2:
                count+=1
            
        return count
