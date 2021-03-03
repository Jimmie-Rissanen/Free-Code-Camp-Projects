# Find the right data and clean it. Add all the floats togheter and print the avarage. 
o = open('mbox.txt', 'r')
f = o.readlines()

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