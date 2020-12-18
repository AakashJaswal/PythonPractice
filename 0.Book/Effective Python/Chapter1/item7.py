# Using Enumerator
sr = 'abcd'

for i, char in enumerate(sr,start=1):
    print(f"{i} {char}")

# Enumarate wrape iterator with a lazy generator.
# Return index and attribute in container