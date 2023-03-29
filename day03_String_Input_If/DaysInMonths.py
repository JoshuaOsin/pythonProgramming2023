number = 12

has28Days = number == 2
has30Days = number == 4 or number == 6 or number == 9 or number == 11

if 1 <= number <= 12:
    if has28Days:
        print('month has 28 days')
    elif has30Days:
        print('month has 30 days')
    else:
        print('month has 31 days')
else:
    print('invalid number')
