class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if len(p) > len(s):
            return res
        
        thash = {}
        for n in p:
            if n in thash:
                thash[n] += 1
            else:
                thash[n] = 1
                
        counter = len(thash)
        b,e = 0,0
        
        while e < len(s):
            if s[e] in thash:
                thash[s[e]] -= 1
                if thash[s[e]] == 0:
                    counter -= 1
            e += 1
            while counter == 0:
                if s[b] in thash:
                    thash[s[b]] += 1
                    if thash[s[b]] > 0:
                        counter += 1
                if  e-b == len(p):
                    res.append(b)
                b += 1
        return res
                
        
