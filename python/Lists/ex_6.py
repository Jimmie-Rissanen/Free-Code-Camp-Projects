
li = []

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    li.append(num)

print('Maximum:', max(li), 'Minimum', min(li))