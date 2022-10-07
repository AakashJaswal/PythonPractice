# Using Enumerator
sr = 'abcd'
d = {'a': 'b', 'c': 'd'}
for i, (key, val) in enumerate(d.items()):
    print(f"{i}: {key} {val}")


for i, char in enumerate(sr,start=1):
    print(f"{i} {char}")

# Enumerate wrap iterator with a lazy generator.
# Return index and attribute in container
