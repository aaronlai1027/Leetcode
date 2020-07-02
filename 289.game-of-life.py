class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                count = 0
                for I in range(max(0,i-1),min(m,i+2)):
                    for J in range(max(0,j-1),min(n,j+2)):
                        if board[I][J] in [1,2]:
                            count+=1
                count -= board[i][j]
                if board[i][j] == 1 and count not in [2,3]:
                    board[i][j] = 2
                if board[i][j] == 0 and count == 3:
                    board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j]%2
                                                              
# 0 dd
# 1 ll                            
# 2 ld
# 3 dl                            
