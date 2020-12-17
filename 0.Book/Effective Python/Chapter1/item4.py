# Item 4: Prefer Interpolated F-Strings

# C-style formatting
a = 2.231231
b = 'string'
dig = 3

print('Int: %f and string: %s' % (a, b))

# F-String
print(f'Int: {a:.{dig}f} and string: {b}')
