class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans = 0
        b,e = 0,0
        shash = {}
        count = 0
        while e < len(s):
            if s[e] in shash:
                shash[s[e]] += 1
            else:
                shash[s[e]] = 1
                
            if shash[s[e]] > 1:
                count += 1
            e += 1
            while count > 0:
                if shash[s[b]] > 1:
                    count -= 1
                shash[s[b]] -= 1
                
                b += 1
            ans = max(ans,e-b)
        return ans
