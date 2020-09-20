# product, permutation, combination(with without replacement)
# INFINITE iterators count, cycle, repeat
from itertools import product, groupby

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(f'{list(prod)=}')

# Groupby(obj, logic to run on it)
person = [{'Name': 'Jim', 'Sales': 23}, {'Name': 'Dwight', 'Sales': 30}, {'Name': 'Andy', 'Sales': 3},
          {'Name': 'Micheal', 'Sales': 60}]
result = groupby(person, key=lambda pair_of_val: 'Top$' if pair_of_val['Sales'] > 20 else 'Bottom$')

for key, val in result:
    print(f'{key=} {list(val)=}')
