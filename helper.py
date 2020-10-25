# some lib which i think give an edge

import timeit

# let's check how much time it take to create a list 10000 time ?
print(f'{timeit.timeit(stmt="[1,2,3,4,5]", number=10000)=} Sec')

import sys

lst = [1, 2, 3, 4, 5]
print(f'{sys.getsizeof(lst)=} bytes')

print(f'{id(lst)=}')

# Todo: Add about functional params
# Todo: multithreading and multiprocessing
