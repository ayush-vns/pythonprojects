d = {1: "one", 2: "two"}
print(d)
print(d[1])
# print(d[7])
print(d.get(2))
print(d.get(8))
print(d.get(9, 0))
print(d.get(1, 0))
# Add to dictionary
d[10] = "ten"
print(d)
print(d.keys())
print(d.values())
print(d.items())
for key, value in d.items():
    print(key, value)

for key in d.keys():
    value = d[key]
    print(key, value)
# Remove
d.pop(2)
print(d)
d.clear()
print(d)
