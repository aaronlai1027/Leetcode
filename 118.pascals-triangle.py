class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            pascal.append([1]*(i+1))
        for i in range(numRows):
            for j in range(1,i): #excluding the edges
                pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
        return pascal
            
