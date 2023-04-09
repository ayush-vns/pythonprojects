a = [1, 2, 3, 2]
b = [5, 1, 2, 9]
common = []
for x in a:
    if x in b and x not in common:
        common.append(x)
print(common)
