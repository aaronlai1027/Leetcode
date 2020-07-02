class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        water = 0
        
        while left < right:
            water = max(water,min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return water
        
        
        
        
        # n = len(height)
        # res = 0
        # for i in range(n):
        #     for j in range(i,n):
        #         water = min(height[i],height[j])*(j-i)
        #         res = max(res,water)    
        # return res
