name = input('Please enter your name: \n')
hourlyRate = int(input('Please enter hourly rate: \n'))
weeklyHours = int(input('Please enter weekly hours: \n'))

print(f'{name}\'s Salary is : $ {hourlyRate*weeklyHours*52}')
