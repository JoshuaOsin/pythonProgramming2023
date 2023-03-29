tuple1 = (1, 2, 3, 4, 4, 3, 6)
list1 = [1, 2, 3, 4, 4, 3, 6]
set1 = {1, 2, 3, 4, 4, 3, 6}

print(tuple1)
print(list1)
print(set1)

result = set(tuple1)
print(result)

result = list(tuple1)
result.append(9)
print(result)
