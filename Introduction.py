# Arrays are one of the most commonly-used data structures
# The elements of an array are stored in contiguous memory locations
# Arrays are of two types : static and Dynamic
# Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
# In Python , there are only dynamic arrays
# Some basic operations and their complxcities are given below:

# Look-up/ Access -O(1)
# Push/Pop - O(1)*
# Insert - O(n)
# Delete - O(n)

array=[5,8,2,9,17,43,25,10]

# Look-up/Acces
# Any element of an array can be accessed by its index.
# we just need to ask for the particular index of the element we are interested in and we will get the element in constant time

first_element = array[0]
sixth_element = array[5]


# Push/pop
# Push corresponds to pushing or adding an element at the end of the array
# Similary, pop corresponds to removing the element at the end of the array
# Since the index of the end of the array is known, finding it and pushing or popping an element will only require O(1) time

array.append(87)

# In some speical cases, the append(push) operation may take greater time. This is because as mentioned earlier, Python has dynamic arrays
# So when an element is to appended and the array is filled, the entire array has to be copied to a new location
# With some space allocated (generally double the space) this time so that more items can be appended.
# Therefore, some individual operations may require O(n) time or greater, but when averaged over a large number of operations, 
# The complexity can be safely considered to be O(1)

array.pop()

print(array)

# Insert
# Insert operation inserts an element at the beginning of the array, or at any location specified.
# This is O(n) operation since after inserting the element at the desired location,
# The elements to the right of the array have to be updated with the correct index as they all have to shifted by one place.
# This requires looping through the array. Hence, O(n) time.

array.insert(0,50) 
array.insert(4,0)

print(array)

# Delete
# Similar to insert, it delets an element from the specified location in O(n) time.
# The elements to the right of the deleted element have to shift one space left, which requires looping over the entire array
# Hence, O(n) time complexity

array.pop(0)
print(array)
array.remove(17)
print(array)
del array[2:4]
print(array)
