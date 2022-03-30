# depite of pre-defined array form in Python
# code below implements our own array.
# using common methods like access,push,pop,insert,delete.


class MyArray():
	def __init__(self):
		self.length = 0 # initialize the array's length to be zero
		self.data={} # initialize teh data of the array using an empty dictionary.keys: index, values:data

	# The attributes of the array class are stored in a dictionary by default
	# when the __dict__ method is called on an instance of the class, it returns the attributes of the class along with their values in a dictionary format
	# when the instance of the class is printed, it returns a class object with its location in memory.
	# but we know when we print the array we get the elements of the array as output
	# when we print the instance of the class, the built in __str__ method is called. So we can modify the __str__method inside the class
	# To suit for needs.


	def __str__(self):
		# this will print the attributes of the array class (length and data) in string format when print (array_instance)is executed
		return str(self.__dict__)


	def get(self,index):
		# This method takes in the index of the element as a parameter and returns the corresponding element in O(1) time
		return self.data[index]


	def push(self,item):
		self.length += 1
		# Adds the item provided to the end of the array
		self.data[self.length - 1] = item


	def pop(self):
		last_item = self.data[self.length - 1] # The last item
		del self.data[self.length - 1] 
		self.length -= 1
		return last_item


	def insert(self,index,item):
		self.length += 1
		for i in range(self.length-1, index, -1):
			# shift all the items after index one location down.
			self.data[i] = self.data[i-1]
		self.data[index] = item


	def delete(self,index):
		for i in range(index,self.length-1):
			# shift all the items after index one location up.
			self.data[i] = self.data[i+1]
		# delete the last element after being shifted forward.
		del self.data[self.length-1]
		self.length -=1


arr=MyArray()
arr.push(6)
# print(arr)

arr.push(2)
# print(arr)

arr.push(9)
# print(arr)

arr.pop()
# print(arr)

arr.push(45)
arr.push(12)
arr.push(67)
# print(arr)

arr.insert(3,10)
# print(arr)

arr.delete(4)
# print(arr)

print(arr.get(1))

print(arr)