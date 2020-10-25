import sys

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

tup_for_mem = "a", "b", 1, 1
list_for_mem = ["a", "b", 1, 1]
print(f'{sys.getsizeof(tup_for_mem)=}')
print(f'{sys.getsizeof(list_for_mem)=}')
# Tuple take a less space

# using tuple to swap value without using temp
a = 4
b = 3
print(a, b)

# this show how tuple packing and unpacking helps switching variable without any temp value
b, a = a, b
print(a, b)

# Fibonacci with this way

i = int(input("Enter no."))

a, b, count = 0, 1, 0

while count < i:
    print(f"{a}", end=" ")
    a, b, count = b, a + b, count + 1
