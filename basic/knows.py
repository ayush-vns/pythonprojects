def knows(a, b):
    known = {0: [1, 2], 1: [2, 3], 2: [4], 3: [2], 4: [1]}
    d = known.get(a)
    if d is None:
        return False
    if b in d:
        return True
    return False
def findCelebrity(p):
    for i in p:
        found = False
        for j in p:
            
if i == j:
continue
if knows(i, j):
found = True
break
if not found:
return i
return -1

people = {0, 1, 2, 3, 4}
print(findCelebrity(people))


