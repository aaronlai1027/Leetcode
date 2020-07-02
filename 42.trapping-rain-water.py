class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        leftMax = 0
        rightMax = 0
        left = 0
        right = len(height) - 1
        while left<right:
            if height[left] < height[right]:
                leftMax = max(leftMax,height[left])
                water = water + leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax,height[right])
                water = water + rightMax - height[right]
                right -= 1
                
        return water
