a = [16, 0, 1, 9, 70]
print(a)
# a.sort(reverse=True)
b = sorted(a, reverse=False)
print(a, b)
a = ["cat", "dog", "ball", "apple"]
a.sort(key=len)
print(a)
a.sort(key=len, reverse=True)
print(a)


def lastchar(s):
    return len(s)


a.sort(key=lastchar)
print(a)
