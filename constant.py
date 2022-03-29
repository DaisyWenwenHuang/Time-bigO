#  O(1) Constant time
# Getting a value at a particular index from an array

import time

s_array = ['small' for i in range(10)]
m_array = ['medium' for i in range(5000)]
l_array = ['large' for i in range(5000000)]


def run_time_cal(array):
    t0 = time.time()
    print(array[0])
    print(array[1])
    t1 = time.time()
    print(f'Tiem taken = {t1-t0}')


run_time_cal(s_array)
run_time_cal(m_array)
run_time_cal(l_array)

# compair the runtime of three cases, they are very close.
# Any constant number can be considered as 1. There we can say this function is of O(1) -constant Time complexity
