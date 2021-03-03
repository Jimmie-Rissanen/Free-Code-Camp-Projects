weight = input('Enter weight: ')
unit = input('K or L?')

if unit.upper() == 'K':
    print(int(weight) / 0.45)
if unit.upper() == 'L':
    print(int(weight) * 0.45)