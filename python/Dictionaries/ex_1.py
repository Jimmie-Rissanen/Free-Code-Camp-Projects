fhand = open('words.txt')

files = dict ()

for line in fhand:
    words = line.split()
    for word in words:
        files [word] = ''

while True:
    print('Write "stop" to exit ')
    ask = input('Ask if word in is string: ')
    if ask == 'stop':
        break
    print(ask in files)

