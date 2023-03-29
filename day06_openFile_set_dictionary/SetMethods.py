set2= {'A'}
set2.add('B')
print(set2)

set2.remove('A')
print(set2)

set2.add('C')
set2.add('C')
print(set2)

set2.update('D','E')
print(set2)
set3 ={'E','F'}

set4 = set2.intersection(set3)
print(set4)

set5 = set2.difference(set3)
print(set5)