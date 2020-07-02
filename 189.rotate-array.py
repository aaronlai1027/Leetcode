class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """O(k*n)
        for i in range(k):
            tmp = nums.pop()
            nums.insert(0,tmp)
        """
        
        def reverse(start, end):
            while start < end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start += 1
                end -= 1
        n = len(nums)
        k = k%n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
