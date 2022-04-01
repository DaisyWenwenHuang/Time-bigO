# Given an interger array nums, find the contigous subarray
# Contaning at least one number, wich has the largest sum
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum of 6

# Brute force solution:
# Find every possible subarray and cal the sum, and return the maximum value
# It is not very efficient but will work
# Time complexity is O(n^2)
# code:

array = [-2,1,-3,4,-1,2,1,-5,4]
array1= [-3,-1,-3,-5,-6,-2]


def brute_force_sol(array):
	# initial maximum can not be set 0 as it is a big assumption that the array can not be all negative
	maximum =array[0]
	if len(array) == 0:
		return None
	for i in range(len(array)):
		cum_sum = 0
		for j in range(i,len(array)):
			cum_sum += array[j]
			maximum = max(maximum, cum_sum)
	return maximum


# print(brute_force_sol(array1))

# Can we improve it?
# if the prefix  (sum before the number) is negative
# get ride of the prefix as joining 'negative subarray' is smaller than the number itself
# iterate the all the number in the array, get ride of negative prefixes.
# 'sliding window'
# Time complexity is O(n)

def pre_fix_sol(array):
	maximum = array[0] # Can not be 0 as number can be negative
	c_sum = 0
	for num in array:
		if c_sum < 0:
			c_sum = 0
		c_sum += num	# This code needs to be behind the reset of the c_sum
		maximum = max(maximum,c_sum)
	return maximum


print(pre_fix_sol(array))


# Kadena's Algorithm approach


def kadena_sol(array):
	maximum = array[0]
	currsum = 0
	for num in array:
		currsum += num
		maximum = max(maximum, currsum)
		if currsum < 0:
			currsum = 0
	return maximum 


print(kadena_sol(array1))



