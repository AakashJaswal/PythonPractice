import sys
def my_generator():
    yield 1
    yield 2
    yield 2


g = my_generator()
print(g)
# above statements returns a generator class which is an iterator.
# hence we can lazily calculate values.

print(next(g))
print(next(g))
print(next(g))


# in depth look
def generator_example(n):
    i = 0
    while i < n:
        yield i
        i += 1

# for sum it'll print result quickly but in actual it lazily produce value
print(sum(generator_example(10)))

# generator expression are same as list comprehension but with ()

my_gen_expr = (i for i in range(100000))
print(sys.getsizeof(my_gen_expr))

my_list_expr = [i for i in range(100000)]
print(sys.getsizeof(my_list_expr))

