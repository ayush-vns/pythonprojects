a = [1, 2, 1, 1, 3, 3, 0, 0, 0, 0]
counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in a:
    counter[i] += 1
    # print(counter)
n = len(counter)
for i in range(n):
    value = counter[i]
    if value > 0:
        print(i, ":", value, end=",")
