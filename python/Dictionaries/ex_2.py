fhand = open('mbox.txt')

dictionary = dict()

for line in fhand:
    line.strip()
    if not line.startswith('From') or len(line) < 0:
        continue
    elif line.startswith('From:'):
        continue
    else:
        words = line.split()
        day = words [2]
        dictionary [day]= dictionary.get(day,0) + 1
print(dictionary)