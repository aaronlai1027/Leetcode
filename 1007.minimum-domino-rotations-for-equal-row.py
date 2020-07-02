class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        countA, countB, same = [0]*7, [0]*7, [0]*7
        for i in range(len(A)):
            countA[A[i]] += 1
            countB[B[i]] += 1
            if A[i] == B[i]:
                same[A[i]] += 1
        for i in range(7):
            if countA[i] + countB[i] - same[i] == len(A):
                return len(A) - max(countA[i],countB[i])
        return -1
