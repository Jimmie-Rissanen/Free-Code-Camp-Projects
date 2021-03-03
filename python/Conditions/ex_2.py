hours = input('Enter hours: ')

try:
    hours_float = float(hours)
except:
    print('Error, please enter a number.')
    quit()

rate = input('Enter rate: ')

try:
    rate_float = float(rate)
except:
    print('Error, please enter a number.')
    quit()

if hours_float >= 40:
    new_hours = hours_float - 40
    over_hours = new_hours * 1.5
    print('Overtime:', (hours_float * rate_float) + over_hours)
else:
    print('Regular:', hours_float * rate_float)