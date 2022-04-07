# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
s="01001001101"

def minflip(s):
	n = len(s)
	s = s + s
	res = len(s)

	alt1 = ''.join(['1' if i % 2 else '0' for i in range(len(s))])
	# print(alt1)
	alt2 = ''.join(['0' if i % 2 else '1' for i in range(len(s))])
	# print(alt2)
	diff1,diff2 = 0,0
	l = 0

	for r in range(len(s)):
		# print(r)
		if s[r] != alt1[r]:
			diff1 += 1
		if s[r] != alt2[r]:
			diff2 += 1

		if (r - l + 1) > n:
			if s[l] != alt1[l]:
				diff1 -= 1
			if s[l] != alt2[l]:
				diff2 -= 1
			l += 1

		if (r - l + 1) == n:
			res = min(res,diff1,diff2)
			# print(res)
	return res



	
print(minflip(s))
