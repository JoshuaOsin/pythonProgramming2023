days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print(days[0])
print(days[-1])

print('---------------------')

for each in days:
    print(each)
print('---------------------')

i = 6
while i >= 0:
    print(days[i])
    i -= 1

print('-------Weekdays--------')

tuple1 = days[:5]
for each in tuple1:
    print(each)

print('-------Weekend--------')

tuple2 = days[5:]
for each in tuple2:

    print(each)

#merge tuples
tuple3 = tuple1+tuple2
for each in tuple3:
    i = tuple3.index(each)
    print(f'{i+1}.{each}')