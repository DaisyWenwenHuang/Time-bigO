# find if the array contains duplicate elements in an array of integers
# return True if yes (appears at least twice), else return False
# Example 
# Input: [1,2,3,1,] output: True
# Input: [1,2,3,4,] output: False

# brute-forse approach
# iterate each element from the beginning and compair with the rest of the array. if match, break the loop and return True. If there is no match after compaied all the elements ,return false.
# this is not very efficient with the time complxity of O(n^2) and space O(n^2)
array = [1,2,46,32,98,61,34,46]


def brute_force_duplicate_search(array):
	for i in range(len(array)-1):
		for j in range(i + 1,len(array)):
			if array[i] == array[j]:
				return True
	return False


print(brute_force_duplicate_search(array))