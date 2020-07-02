class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)-1
        
        while left <= right:
            mid = (left+right)//2
            if citations[mid] == len(citations) - mid:
                return citations[mid]
            elif citations[mid] > len(citations)-mid:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations)-left
        # n = len(citations)   
        # start, end = 0, n-1  
        # while start <= end:  
        #     middle = (start + end) // 2  
        #     if citations[middle] == n-middle: return citations[middle]  
        #     elif citations[middle] < n - middle: start = middle + 1  
        #     else: end = middle - 1  
        # return n-end-1  
