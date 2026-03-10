d1 = {1: 25, 2: 75, 3: 95}
d2 = {3: 300, 4: 10, 5: 65}
print("Dictionary 1:", d1)
print("Dictionary 2:", d2)
mergeor = dict(d1.items() | d2.items())
print("\nMerged using | operator:", mergeor)
mergeunpack = {**d1, **d2}
print("Merged using unpacking:", mergeunpack)
mergeupdate = d1.copy()
mergeupdate.update(d2)
print("Merged using update():", mergeupdate)
mergeloop = d1.copy()
for k, v in d2.items():
    mergeloop[k] = v
print("Merged using for loop:", mergeloop)
