class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        A = [0]+A
        d = collections.deque()
        d.append(0)
        res = len(A)
        for i in range(1,len(A)):
            A[i] += A[i-1]
            while d and A[i] <= A[d[-1]]:
                d.pop()
            while d and A[i] - A[d[0]] >= K:
                res = min(res, i - d.popleft())
            d.append(i)
        return -1 if res == len(A) else res
