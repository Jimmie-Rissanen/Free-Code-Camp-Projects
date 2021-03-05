fhand = open('mbox.txt')

counts = dict()

for line in fhand:
    if not line.startswith('From') or len(line) < 0:
        continue
    elif line.startswith('From:'):
        continue
    else:
        line.rstrip()
        words = line.split()
        time = words [5]
        time = time.split(':')
        hour = time [0]
        counts [hour] = counts.get(hour , 0) +1 

common_hour = []

for key, value in counts.items():
    common_hour.append((value, key))
common_hour.sort(reverse = True)

for key, value in common_hour:
    print(f'Most sent:{key}, time: {value}')