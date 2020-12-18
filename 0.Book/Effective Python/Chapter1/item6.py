# Use unpacking over indexing

snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]

for (item, cal) in snacks:
    print(f"{item} contains {cal} cal")