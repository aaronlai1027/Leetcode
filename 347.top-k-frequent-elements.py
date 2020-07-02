class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        c = collections.Counter(nums)

        bucket = []
        for _ in range(len(nums)):
            bucket.append([])

        for i, v in c.items():
            bucket[-v].append(i)

        for i in range(len(bucket)):
            if len(res) < k:
                res += bucket[i]
            
        return res
            
        #ind = 0
       # while len(res) < k:
         #   res += bucket[ind]
          #  ind += 1
        #return res
