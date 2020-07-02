class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)        
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]  == target:
                return mid
            elif nums[mid] > nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if target > nums[mid] and target < nums[left]:
                    left = mid + 1
                else:
                    right = mid
        return -1
