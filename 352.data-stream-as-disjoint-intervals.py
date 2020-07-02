class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []

    def addNum(self, val: int) -> None:
        if not self.res: self.res.append([val,val])
        i = 0
        
        while i < len(self.res) and val >= self.res[i][1]+1:
            i += 1
        if i == 0:
            if val >= self.res[0][0]-1:
                self.res[0][0] = min(val,self.res[0][0])
            else:
                self.res.insert(0,[val,val])
        elif i == len(self.res):
            if val == self.res[i-1][1]+1:
                self.res[i-1][1] = val
            else:
                self.res.append([val,val])
        elif val == self.res[i-1][1]+1 and val == self.res[i][0]-1:
            self.res[i-1][1] = self.res[i][1]
            self.res.pop(i)
        elif val >= self.res[i][0]-1:
            self.res[i][0] = min(val,self.res[i][0])
        elif val == self.res[i-1][1]+1:
            self.res[i-1][1] = val
        else:
            self.res.insert(i,[val,val])
        
            
    def getIntervals(self) -> List[List[int]]:
        return self.res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
