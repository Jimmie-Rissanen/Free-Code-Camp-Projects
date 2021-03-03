
num = None
count = 0
total = 0
while True:
    num = input('Enter a number: ')
    try:
        num = int(num)
        count = count + 1
        total = total + num
    except:
        if num == 'done':
            break
        else:
            print('Not a number..')
            continue    
print(total, count, total / count)