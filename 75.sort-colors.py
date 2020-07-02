class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        lt,i,gt = 0,0,len(nums)-1
        while True:
            if i > gt:
                return nums
            elif nums[i] < pivot:
                nums[i],nums[lt] = nums[lt],nums[i]
                i+=1
                lt+=1
            elif nums[i] > pivot:
                nums[i],nums[gt] = nums[gt],nums[i]
                gt-=1
            else:
                i+=1
                
