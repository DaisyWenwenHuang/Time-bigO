# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counT,window = {},{}
        res= []
        n = len(s)
        m = len(p)
        
        if m >n:
            return []
        for i in range(m):
            counT[p[i]] = 1 + counT.get(p[i],0)
                    # initial the fixed length window
            window[s[i]] = 1+ window.get(s[i],0)
        if counT==window:
            res.append(0)

        
        # loop 
        lp=0
        for r in range(m,n):
            window[s[r]] = 1 + window.get(s[r],0)
            window[s[lp]] -= 1
            
            if window[s[lp]]==0:
                window.pop(s[lp])
            lp += 1
            if counT == window:
                res.append(lp)
        return res