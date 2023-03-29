name = input('Please enter your name: \n')
buildingNumber = int(input('Please enter building number: \n'))
streetName = input('Please enter street name: \n')
city = input('Please enter city name: \n')
state = input('Please enter state name: \n')
zipCode = int(input('Please enter zip code: \n'))

print('Your Shipping Adress is ')
print(f'\t{name.title()}\n'
      f'\t{buildingNumber} {streetName.title()}\n'
      f'\t{city.capitalize()} {state.upper()} {zipCode}')