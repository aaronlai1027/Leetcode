class Solution:
    def hIndex(self, citations: List[int]) -> int:
        bucket = [0]*(len(citations)+1)
        for num in citations:
            if num >= len(citations):
                bucket[len(citations)]+=1
            else:
                bucket[num]+=1
        print(bucket)
        count = 0
        for i in range(len(bucket)-1,-1,-1):
            count += bucket[i]
            if count >= i:
                return i
            
        return 0
