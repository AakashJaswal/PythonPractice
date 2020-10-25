# ORDERED, MUTABLE with DUPLICATE ELEMENTS
# Stack = FIFO, list can be used as stack using append and pop.
# list comprehension kinda works like lambda syntax
# syntax for list comprehension  = [output_expression for element in iterable if some_condition]

list1 = [1, 2, 3, 4, 5, 6]
list2 = [element + element for element in list1]
print(id(list1))
print(id(list2))
print(list2)

# i can also maybe make this dict ?
dict1 = {f'key{key}': key + 1 for key in list1}
print(id(dict1))
print(dict1)
# Yes i can :D

# let's try to take sum and store it in dict key
sum_dict = {'Sum': 0}
y = lambda x, y: x + y
sum_dict = {'Sum': y(sum_dict['Sum'], val) for val in list1}

print(sum_dict)
# Interesting just take last result

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12], ]
print([[row[i] for row in matrix] for i in range(4)])

print([num for row in matrix for num in row])