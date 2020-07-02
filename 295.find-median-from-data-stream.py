class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = []
        self.small = []
        
    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.small,-heapq.heappushpop(self.large,num))
        else:
            heapq.heappush(self.large,-heapq.heappushpop(self.small,-num))
        
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0])/2
        else:
            return -self.small[0]
         
        
        
        
        
#     def addNum(self, num: int) -> None:
#         self.numList.append(num)
#         self.numList = sorted(self.numList)

#     def findMedian(self) -> float:
#         l = len(self.numList) 
#         if l%2 == 1:
#             return self.numList[l//2]
#         else:
#             return (self.numList[l//2-1]+self.numList[l//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
