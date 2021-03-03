# Add a little joke to the code. 

inp = input('Enter file name: ')
try:
    o = open(inp)
    f = o.readlines()
except:
    if inp == 'Baab':
        print('Not event funny...')
        quit()
    else:
        print('No such file in directory.')
        quit()

l = []
count = 0
total = 0

for line in f:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        line = line.rstrip()
        ind = line.find(':')
        line_float = float(line [ind + 2 : ])
        total = total + line_float
        
print(total / count)