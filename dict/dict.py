# Mutable, unordered, key:val

# you don't have to give quotes with dict() keyword
dict1 = {"Name": "M.Scott", "Pos": "Manager"}
dict2 = dict(name='Jim', pos='Salesman')

print(f"{dict1=}")
print(f"{dict2=}")

for key, val in dict1.items():
    print(f'{key=} {val=}')

# If key's a num we can't fetch stuff with index coz then it'll interpret it as key
# Key should be immutable i.e., it should be hashable. hence you can't use list
