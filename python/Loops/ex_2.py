num = 0
largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    try: 
        num = int(num)
    except:
        if num == 'done':
            break
        print('Not a number...')
        continue
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num 
print('Largest:', largest, 'Smallest:', smallest)