
grocery_list = ['Eggs', 'Apples', 'Rice', 'Milk']

print( len(grocery_list) )

grocery_list.append('Beef')

grocery_list.append('Peanut')

print( len(grocery_list) )

print(grocery_list)

grocery_list[1] = 'Cherry'
grocery_list[-1] = 'Chicken'

print(grocery_list)

grocery_list.append('Eggs')
grocery_list.append('Eggs')

print(grocery_list)

grocery_list.remove('Rice')
print(grocery_list)

print(f'the number of Eggs in the list is {grocery_list.count("Eggs")}')

