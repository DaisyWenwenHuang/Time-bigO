# https://leetcode.com/problems/permutation-in-string/
# premutations of a string are different orderings of a string
# for example "abc", its permutation can be  ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      # counttable for s1 and sliding window to track targeted letters
        countS = {}
        countW = {}
        m = len(s1)
        if m > len(s2):
            return False
        
        for i in range(m):
            countS[s1[i]] = 1 + countS.get(s1[i],0)
            countW[s2[i]] = 1 + countW.get(s2[i],0)
            
        if countS == countW:
            return True
        
        l = 0
        for r in range(m,len(s2)):
            countW[s2[r]] = 1 + countW.get(s2[r],0)
            # needs to check if the element count is equal to 0 after decreas one
			countW[s2[l]] -= 1
            if countW[s2[l]] == 0:
                countW.pop(s2[l])
            if countS == countW:
                return True

            l += 1
        return False

# better solution
# can iterate the two lists, s1 and s2,
# make two count hashmaps to compair how many matehces are there
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      # counttable for s1 and sliding window to track targeted letters
        # using list 
        countS = [0] * 26
        countW = [0] * 26
        
        m = len(s1)
        if m > len(s2):
            return False
        
        for i in range(m):
            # ord() to get the ascii integer of the letter
            # subtract the ascii integer of a which makes the index of letter
            # a 0, and b 1, etc.
            countS[ord(s1[i]) - ord('a')] += 1
            countW[ord(s2[i]) - ord('a')] += 1
        
        match = 0
		# T(26)
        for i in range(26):
            if countS[i] == countW[i]:
                match += 1
        
        l = 0
		# T(n)
        for r in range(m, len(s2)):
            if match == 26:
                return True

			# sliding fixed length window 
            index = ord(s2[r]) - ord('a')
            countW[index] += 1
            if countW[index] == countS[index]:
                match += 1
            elif countW[index] == countS[index] + 1:
                match -= 1
                
            index = ord(s2[l]) - ord('a')
            countW[index] -= 1
            if countW[index] == countS[index]:
                match += 1
            elif countW[index] == countS[index] - 1:
                match -=1
            l += 1
        return match == 26
                