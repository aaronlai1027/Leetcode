class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        low = 0
        high = n1
        
        while(low<=high):
            partition1 = (low+high)//2
            partition2 = (n1+n2+1)//2-partition1
            
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1-1]
            minRight1 = float('inf') if partition1 == n1 else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2-1]
            minRight2 = float('inf') if partition2 == n2 else nums2[partition2]
        
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (n1+n2)%2 == 1:
                    return max(maxLeft1,maxLeft2)
                else:
                    return (max(maxLeft1,maxLeft2) + min(minRight1,minRight2))/2
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1
        
        
        

        
        
# XXXXX m-1 m XXX
# YYYYY m-1 m YYYY

# ZZZZZZZZZZ

# if not num1: 
    
# a > b: get(num1,num2[2/k+1:],2/k)
