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

squared_list_2 = map(lambda x: x*x, num_list)
print(list(squared_list_2))
