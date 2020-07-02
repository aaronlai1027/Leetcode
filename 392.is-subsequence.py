class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        i = 0
        l = len(s)
        for char in t:
            if i < l and char == s[i]:
                i += 1
            if i == l:
                return True
        return False
