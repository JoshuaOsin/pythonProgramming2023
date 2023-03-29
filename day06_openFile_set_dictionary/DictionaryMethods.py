employee1 = {
    'name': 'Joshua',
    'gender': 'M',
    'age': 48,
    'salary': 23000
}

print(employee1.get('name'))
print(employee1['name'])

employee1['name']= 'Jane'
print(employee1.get('name'))

employee1.update({'name':'Joshua'}) #use : for pair, not preferred
print(employee1.get('name'))

employee1['department']= 'Support Team'
print(employee1)

employee1.pop('salary')
print(employee1)

employee1.popitem() #last item will be removed
print(employee1)


