s = "apple"
print(s)
print(s[0])
print(s[3])
print(s[-1])
print(s[-2])


def lastChar(s):
    return s[-1]


a = ["sachin", "rahul", "amit"]
a.sort(key=lastChar)
print(a)
# Using lambda
a.sort(key=lambda x: len(x), reverse=True)  # Sorting by last character and reverse
print(a)

k = "mango"
print(k)
print(k[-3])
