# no duplicate, mutable, unordered
set_1 = {1, 2, 3, 1, 2}
print(f'{set_1=}')
set_with_list = set([1, 2, 3, 4, 5, 5, 4, 6])
print(f'{set_with_list=}')
set_with_string = set('hello')
print(f'{set_with_string=}')

empty_set = set()  # can't use {}, it'll assume it as dict

# use set.discard to del, rather than set.remove
# leverage union, intersect, diff
# Symmetric_difference will remove common ele and return result intersection_update will return common ele

#FROZEN Set no duplicate, immutable, unordered