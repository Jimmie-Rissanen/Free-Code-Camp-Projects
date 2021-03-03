hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

if hours >= 40:
    new_rate = (hours - 40) * 1.5
    over_rate = (hours * rate) + new_rate
    print('overtime pay:', over_rate)
else:
    print('regulare pay:', hours+rate)