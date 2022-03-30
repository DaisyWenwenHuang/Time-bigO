# find if the array contains duplicate elements in an array of integers
# return True if yes (appears at least twice), else return False
# Example 
# Input: [1,2,3,1,] output: True
# Input: [1,2,3,4,] output: False

# brute-forse approach
# iterate each element from the beginning and compair with the rest of the array. if match, break the loop and return True. If there is no match after compaied all the elements ,return false.
# this is not very efficient with the time complxity of O(n^2) and space O(n^2)
array = [1,2,46,32,98,61,34,46]
array1 = [1,2,46,32,98,61,34]


def brute_force_duplicate_search(array):
	for i in range(len(array)-1):
		for j in range(i + 1,len(array)):
			if array[i] == array[j]:
				return True
	return False


# print(brute_force_duplicate_search(array))
# print(brute_force_duplicate_search(array1))

# how to imporve the brute_force solution with better time complxity cand memory usage?
# can we sort it first?  If yes, can just using one loop, compaire elemnts with its next one.  reduce time to O(nlog n) (sort function is O(nlongn), loop is O(n))


def better_duplicate_search(array):
	array.sort()
	for i in range(len(array)-1):
		if array[i]==array[i+1]:
			return True
	return False


# print(better_duplicate_search(array))
# print(better_duplicate_search(array1))

	
# can we improve the function even better?
# dictionary has constant access time of elements, maybe can be useful
# iterate the array and put each element into an dictionary. before put in the dictionary, check if there is already an element with same value exist. if so, return True, if not, put the element in the dicionary. till the end, if no match, return false 
# time would be O(n) 


def hashtable_duplicate_search(array):
	hashtable={}
	for i in range(len(array)):
		if array[i] in hashtable:
			return True
		else:
			hashtable[array[i]]=True
	return False


print(hashtable_duplicate_search(array))
print(hashtable_duplicate_search(array1))
		