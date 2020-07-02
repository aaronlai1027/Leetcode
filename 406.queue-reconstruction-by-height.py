class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        sortedL = sorted(people,key=lambda x:(-x[0],x[1]))
        res = []

        for i in range(len(sortedL)):
            if not res:
                res.append(sortedL[i])
            else:
                res.insert(sortedL[i][1],sortedL[i])
  
        return(res)
    
