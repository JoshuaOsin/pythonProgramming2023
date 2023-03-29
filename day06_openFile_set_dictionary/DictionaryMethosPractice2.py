student1 = {
    'name': 'Joshua',
    'gender': 'M',
    'age': 48,
    'scores': (60, 65, 75)
}

print(student1['scores'][2])
print('--------------')

car1 ={
    'make' : 'Toyota',
    'model': 'Camry',
    'year': 2018,
    'color': 'black',
    'price': 25000
}

for x in car1.keys():
    print(x)


for y in car1.values():
    print(y)

print(list(car1.items()))

print('-----------')

for pair in list(car1.items()):
    print(f'{pair[0]} is {pair[1]}')






