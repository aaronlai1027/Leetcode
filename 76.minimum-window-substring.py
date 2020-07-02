class Solution:
  
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        thash = {}
        for n in t:
            if n in thash:
                thash[n] += 1
            else:
                thash[n] = 1
        
        ans =(float("inf"),None,None)
        
        count = len(thash)
        b,e = 0,0
        while e < len(s):
            if s[e] in thash:
                thash[s[e]] -= 1
                if thash[s[e]] == 0:
                    count -= 1
            
            while count == 0:
                if s[b] in thash:
                    thash[s[b]] += 1
                    if thash[s[b]] > 0:
                        count += 1
                if e-b+1 < ans[0]:
                    ans = (e-b+1,b,e)
                b += 1    
            e += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
            
