# Find the longest word in a given string
# Example :
# Input: 'fun&!! time'
# Output : time

# try some simply way to compair 
# check every character , if it is an alphanumeric character, counter +=1
# if not, counter reset to 0
# tracking a current_max  to find the longest word.


def easy_longest_word(string):
	counter = 0
	current_max = 0
	for char in string:
		if char.isalnum():
			counter += 1
		else:
			current_max = counter
			counter = 0
		longest = max(current_max,counter)
	return longest


string='fun!$@! times'
string1=' fun@#times #app'
# print(easy_longest_word(string))
# This function only prints the number of charcters of the longest word
# Does not print out the word itself.
# How to improve?

# thinking:
# loop the string to check each element,
# if char, counter +=1, if not counter reset to 0.
# counter is tracking the length of each word in the string 
# using a dictionary, tracking the counter at each element
# the max value of the dictionary is the length the of longest word,  
# and its key is the index of the end of the longest word. 
# using slicing to get the word from the string.


def longest_word(string): 
	counter = 0
	# current_max = 0
	D={}
	for i , char in enumerate(string):
		if char.isalnum():
			counter += 1
		else:
			# D[i]=counter
			counter = 0
		D[i]=counter
		# current_max = max(current_max, counter)
	n_ind=max(D,key=D.get)
	n_val=D.get(n_ind)
	word=string[n_ind-n_val+1:n_ind+1]	
	return word

# print(longest_word(string1))

	
# can we use re library?
# would be more efficient 
# thinking :
# first : split the string into groups of words
# then : find the max length word

import re


def regex(string):
	words = re.findall('\w+',string)
	D={}
	for word in words:
		D[word]=len(word)
	# print(D)
	l_word=max(D,key=D.get)
	# print(longest_word)	
	return print(l_word)


regex(string)

		
		






