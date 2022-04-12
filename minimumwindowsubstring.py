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


# 
        if len(t) > len(s):
            return ''
        
        countT={}
        countW={}
        res=[-1,-1]
        res_len = float(inf)

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i] , 0)
        need = len(countT)
        
        l = 0
        have = 0
        for r in range(len(s)):
            countW[s[r]] = 1 + countW.get(s[r], 0)
            if s[r] in countT and countW[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                countW[s[l]] -= 1
                if s[l] in countT and countW[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        if res_len != float(inf):
            return s[l:r+1]
        else:
            return ''
     