import time

fav_color = ['red']
color = ['blue', 'green', 'grey', 'black', 'teal', 'red', 'pruple']
large_array = ['red' for i in range(500000)]


def whatis_fav_color(array):
    red = 0
    t0 = time.time()
    for i in range(len(array)):
        if array[i] == 'red':
            red += 1
            # print('your favorate color is red')
    t1 = time.time()

    print(
        f'It took you {t1-t0} seconds to decide which color is your favorate!')


whatis_fav_color(fav_color)
whatis_fav_color(color)
whatis_fav_color(large_array)


def funchallenge(inpt):
	temp = 10 #O(1)
	temp = temp+50 # O(1)
	a = 0 #O(1)
	for i in range(len(inpt)): #O(n)
		if i:  #n*O(1)
			a += 1 #n*O(1)
 	return print(a) # O(1)

funchallenge(fav_color)
funchallenge(color)
funchallenge(large_array)

# total runing time of the funchallenge function :
#O(1+1+1+n+n*1+n*1+1)=O(3*n+4) becomes O(n)

