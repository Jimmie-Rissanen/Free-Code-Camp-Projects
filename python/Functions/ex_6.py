def compute_pay(hours, rate):
    if hours >=40:
        over_hours = hours - 40
        over_pay= (over_hours * 1.5) + hours * rate
        print('Overtime:', over_pay)
    else:
        pay = hours * rate
        print('Refular:', pay)


hours= float(input('Enter hours: '))
rate= float(input('Enter rate: '))

compute_pay(hours, rate)
