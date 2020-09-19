# Immutable, ordered, text representation
str = '  hello   '
print(f'{str=}')
print(f'{str.strip()=}')
str_comma = "1,2,3,4"
new_ls = str_comma.split(',')
print(new_ls)
str_back = ','.join(new_ls)
print(str_back)

# decimal formatting {:.2f}.format(2.333) = 2.33
