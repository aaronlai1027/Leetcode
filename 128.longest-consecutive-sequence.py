class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        len = 0
        for num in s:
            if num - 1 not in s:
                y = num
                cnt = 0
                while num in s:
                    cnt += 1
                    num += 1
                len = max(len,cnt)
        return len
