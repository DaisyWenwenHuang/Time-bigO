# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        W={}
        l_max = 0

        for r in range(len(s)):
            W[s[r]] = 1 + W.get(s[r],0)
            
            if (r - l + 1) - max(W.values()) <= k:
                l_max = max(l_max,(r - l + 1))
            else:
                W[s[l]] -= 1
                l += 1
            
        return l_max
        