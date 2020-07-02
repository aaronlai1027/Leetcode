class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)

        most = count.most_common()[0][1]

        nofmax = 0
        for v in count.values():
            if v == most:
                nofmax += 1
        
        return max((most-1)*(n+1)+nofmax, len(tasks))
