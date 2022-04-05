# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        lp = 0 # left pointer initially to be 0
        maxlen= 0 # maxlen as result

		# right pointer loop through the list 
        for i in range(len(s)):
			# remove the repeated element and elements in front of it
            while s[i] in subset:
                subset.remove(s[lp])
                lp += 1
            # add the right pointer element into the set
			subset.add(s[i])
			# update the longest length of substring
            maxlen = max(maxlen,i-lp+1)
        return maxlen