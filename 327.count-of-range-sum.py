class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        acc = [0]
        for num in nums:
            acc.append(acc[-1]+num)
        
        def sortTwoSortedArray(nums):
            low = 0
            high = len(nums)
            mid = low + (high-low)//2
            i = 0
            j = mid
            res = []
            while i < mid and j < high:
                if nums[i] < nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j += 1
            if i == mid:
                res.extend(nums[j:high])
            else:
                res.extend(nums[i:mid])
            return res            
        
        def mergeSorted(low,high):
            mid = low + (high-low)//2
            #if there the array has 1 element or empty
            if mid == low: return 0
            
            count = mergeSorted(low,mid) + mergeSorted(mid,high)
            i = j = mid
            for left in acc[low:mid]:
                while i < high and acc[i] - left < lower: i += 1
                while j < high and acc[j] - left <=upper: j += 1
                count += j-i
                
            #To interate i and j in O(n), merge the halves for the sorting. Using "sorted" do that, which uses Timsort and takes O(n) also to recognize and merge the already sorted halves.
            acc[low:high] = sortTwoSortedArray(acc[low:high])
            #acc[low:high] = sorted(acc[low:high])
            return count
        return mergeSorted(0,len(acc))
