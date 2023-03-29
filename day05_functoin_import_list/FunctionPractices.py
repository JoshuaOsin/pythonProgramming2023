def addNumbers(num1, num2):
    print(f'sum of {num1} and {num2} is {num1 + num2}')
    return num1+num2


num3= addNumbers(10, 20)
print(num3*2)


def compareNumbers(num1, num2):
    if num1 < num2:
        print(f'{num2} is maximum')
    elif num1 > num2:
        print(f'{num1} is maximum')
    else:
        print(f'Both numbers are equal')

compareNumbers(20,20)

print('----------------------')

def print_each(sequence):
    for each in sequence:
        print(each)

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print_each(days)