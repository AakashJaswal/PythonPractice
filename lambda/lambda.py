# lambda args: expression
plots = [(2, 3), (3, 1), (2, -1), (-1, 3)]
plots.sort()
print(plots)
# it sorts by 0th index.
# with below lambda we can do custom sort, below i am sorting with y
print(sorted(plots, key=lambda plot: plot[1]))

num_list = [1, 2, 3, 4]
squared_list = [x * x for x in num_list]
print(squared_list)

# Map(func, iterable), basically pass elem from iterable to func and return map object,
# you can make that object to list and get output
squared_list_2 = map(lambda x: x * x, num_list)
print(list(squared_list_2))

# filter(func, iterable), same as map, but return only true results
even_num = filter(lambda x: x % 2 == 0, range(1, 10))
print(list(even_num))

even_num = [x for x in range(1, 10) if x%2==0]
print(even_num)