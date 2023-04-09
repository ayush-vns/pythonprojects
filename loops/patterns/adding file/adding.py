i=[1,2,3,4,5]
i=i+[6]
i=[0]+i
print(i)
i=[1,2,3,4,5]
print("original list",i)
i=i+[6]
print("After right plus",i)
i=[0]+i
print("After left plus",i)
i.append(7)
print("After append",i)
i.extend([8,9,10])
print("after extend",i)