class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
   
        def singleMax(nums,k):
            drop = len(nums)-k
            res = []
            for num in nums:
                while drop and res and res[-1]<num:
                    res.pop()
                    drop -= 1
                res.append(num)
            return res[:k]
            
        
        def merge(nums1,nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:
                    res.append(nums1.pop(0))
                else:
                    res.append(nums2.pop(0))
            return res
        
        res = []
        for i in range(max(0,k-len(nums2)),min(k,len(nums1))+1):
            res = max(res,merge(singleMax(nums1,i),singleMax(nums2,k-i)))
        return res
