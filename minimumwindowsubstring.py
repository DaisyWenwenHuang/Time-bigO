# minimumwindowsubstring.py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counT,window={},{}
        
        
        for ele in t:
            counT[ele]=1+counT.get(ele,0)
        
        need = len(counT)
        have = 0
        res = [-1,-1]
        reslen = float('infinity')
        lp = 0
        
        for rp in range(len(s)):
            char = s[rp]
            window[char]= 1 + window.get(char,0)
            if (char in counT) and (window[char]==counT[char]):
                have += 1
            while have == need:
                if (rp - lp + 1)< reslen:
                    res = [lp,rp]
                    reslen = (rp -lp + 1)
                # pop from the left window
                window[s[lp]] -= 1
                if (s[lp] in counT) and (window[s[lp]] < counT[s[lp]]):
                    have -= 1
                lp += 1
                
        # get the result
        l,r = res
        if reslen != float('infinity'):
            return s[l:r+1]
        else:
            return ''
