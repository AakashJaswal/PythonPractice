# some lib which i think give an edge
import functools

import timeit

# let's check how much time it take to create a list 10000 time ?
print(f'{timeit.timeit(stmt="[1,2,3,4,5]", number=10000)=} Sec')

import sys

lst = [1, 2, 3, 4, 5]
print(f'{sys.getsizeof(lst)=} bytes')

print(f'{id(lst)=}')

# Todo: Add about functional params
# Todo: multithreading and multiprocessing


def super_timer(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print("Start Timing")
        result = f(*args, **kwargs)
        print(f"called function {f} with params {args}, it returned {result}")
        print("End Timing")
        return result
    return wrapper

@super_timer
def add(a,b):
    return a+b

@super_timer
def subtract(a,b):
    return a-b

print(add(2,3))
print(add)
print(subtract(2,3))
print(subtract)