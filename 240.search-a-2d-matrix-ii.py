class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i = 0
        j = len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            pos = matrix[i][j]
            if target > pos:
                i += 1
            elif target < pos:
                j -= 1
            else:
                return True
        return False
