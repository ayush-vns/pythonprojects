s1 = set([1, 2, 3, 4, 5, 5, 5, 5, 5])
s2 = {1, 2, 3, 4}
print(s1, s2)
print(type(s1), type(s2))  # Types of the objects
# Add elements
s1.add(4)  # Add 1  element
print(s1)
s1.update([1, 2, 3, 4, 5, 6, 7, 8])  # Add multiple elements. Duplicates will be rejected
print(s1)
s1.remove(6)  # Remove elements from the set. Raises a KeyError if it doesn't exist
print(s1)
s1.discard(5)  # no error
poppedelement = s1.pop()  # Removes a random element and returns it
print(s1, poppedelement)
s1.clear()  # Removes all elements
print(s1)
cricketers = {"kkr", "rcb"}
footballers = {"rr", "rcb"}
# Union
u = cricketers.union(footballers)  # All elements with duplicates only once
print("Union ", u)
u = cricketers.copy()  # Make a copy
u.update(footballers)
print("Union ", u)
i = cricketers.intersection(footballers)  # Common elements only
print("Intersection ", i)
i = cricketers.copy()
i &= footballers
print("Intersection ", i)
i = cricketers.copy()
i &= footballers
print("Intersection ", i)
diff = cricketers.difference(footballers)  # Elements in cricketers but not in footballers
print("Difference ", diff)
diff = cricketers - footballers  # Same as above
print("Difference ", diff)
symmdiff = cricketers.symmetric_difference(footballers)  # Remove common elements
print("Symmetric Difference", symmdiff)
symmdiff = cricketers.copy()
symmdiff ^= footballers
print("Symmetric Difference", symmdiff)
a = {1, 2, 3}
b = {1, 2}
print("Subset ", a.issubset(b))
print("Subset ", a <= b)
print("Subset ", b.issubset(a))
print("Subset ", b <= a)
print("Superset ", a.issuperset(b))
print("Superset ", a >= b)
print("Superset ", b.issuperset(a))
print("Superset ", b >= a)
# disjoint
a = {1, 2}
b = {3, 4}
c = {1, 2}
print("disjoint ", a.isdisjoint(b))
print("disjoint ", a.isdisjoint(c))
# Update methods
a = {1, 2}
b = {2, 3}
c = {3, 4}
d = a.copy()
d.intersection_update(b)
print("Intersection update ", d)
d = a.copy()
d.difference_update(b)
print("Difference update ", d)
d = a.copy()
d.symmetric_difference_update(b)
print("Symmetric difference update ", d)
