class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)
        i = 0
        j = n-1
        while i < n and intervals[i][1] < newInterval[0]:
            i+=1
        while j >= 0 and intervals[j][0] > newInterval[1]:
            j-=1
        
        if i == n:
            intervals.append(newInterval)
            return intervals
        if j == -1:
            intervals.insert(0,newInterval)
            return intervals
        
        intervals = intervals[:i]+[[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[j][1])]]+intervals[j+1:]
        return intervals
