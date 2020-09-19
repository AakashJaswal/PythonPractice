# Ordered, Immutable, allows duplicate value
tup = "not a string",
print(type(tup))

# Good to get def resp as below
tup_1 = "Micheal", 38, "Manager"
name, age, post = tup_1
print(f'{type(name)=} {name=}')
print(f'{type(age)=} {age=}')
print(f'{type(post)=} {post=}')

# What if i wanted the resp as a list?
*ls, pst = tup_1
print(f'{type(ls)=} {ls=}')
print(f'{type(pst)=} {pst=}')

# let's compare mem with list
import sys

tup_for_mem = "a", "b", 1, 1
list_for_mem = ["a", "b", 1, 1]
print(f'{sys.getsizeof(tup_for_mem)=}')
print(f'{sys.getsizeof(list_for_mem)=}')

# Tuple take a less space
