if True:
    print("Hello World")
print("---------------")
i = 0
while i < 5:
    print("Hello World")
    i += 1
print("---------------")

age = int(input('Please enter your age \n'))
usCitizen = input('Please enter are you US Citizen \n')
while not (usCitizen.upper() == 'YES' or usCitizen.upper() == 'NO'):
    usCitizen = input('Please re-enter are you US Citizen? \n')

if age >= 21 and usCitizen.upper() == 'YES':
    print('You are eligible for vote')
else:
    print('You are not eligible for vote')
