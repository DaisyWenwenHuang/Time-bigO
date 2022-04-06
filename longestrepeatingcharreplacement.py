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

# slitly better one
# diff:
# using f_max to track the current most frequent count of the character
# rather than scan all the count dictionary  to find the max. 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        W={}
        l_max = 0
        f_max = 0
        for r in range(len(s)):
            W[s[r]] = 1 + W.get(s[r],0)
            f_max = max(f_max, W[s[r]])
            if (r - l + 1) - f_max <= k:
                l_max = max(l_max,(r - l + 1))
            else:
                W[s[l]] -= 1
                l += 1
            
        return l_max
        